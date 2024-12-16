import pandas as pd
import numpy as np
from sklearn.datasets import make_blobs
from datetime import datetime, timedelta
import random
import __main__

def generate_keylock_dataset(n_samples=1000, n_locks=10, n_users=50, contamination=0.1, random_state=42):
    """
    Generate synthetic electronic keylock access pattern dataset
    
    Parameters:
    -----------
    n_samples : int
        Number of access events to generate
    n_locks : int
        Number of unique electronic locks in the system
    n_users : int
        Number of unique users
    contamination : float
        Proportion of anomalous events
    random_state : int
        Random seed for reproducibility
    
    Returns:
    --------
    pandas.DataFrame with keylock access patterns
    """
    np.random.seed(random_state)
    random.seed(random_state)
    
    # Calculate number of normal and anomalous samples
    n_anomalies = int(n_samples * contamination)
    n_normal = n_samples - n_anomalies
    
    # Generate base features using make_blobs
    # We'll use these as a base for our temporal patterns
    X_normal, _ = make_blobs(n_samples=n_normal, n_features=2, 
                            centers=1, cluster_std=0.5, 
                            random_state=random_state)
    
    X_anomalies, _ = make_blobs(n_samples=n_anomalies, n_features=2,
                               centers=[[4, 4]], cluster_std=1.5,
                               random_state=random_state)
    
    # Combine normal and anomalous samples
    X = np.vstack([X_normal, X_anomalies])
    
    # Create basic user and lock information
    user_ids = [f'USER_{i:03d}' for i in range(n_users)]
    lock_ids = [f'LOCK_{i:03d}' for i in range(n_locks)]
    
    # Define access levels for users
    access_levels = ['basic', 'advanced', 'admin']
    user_access_levels = {user: random.choice(access_levels) for user in user_ids}
    
    # Define normal working hours (8 AM to 6 PM)
    normal_hours = list(range(8, 19))
    
    # Generate timestamps
    base_timestamp = datetime.now() - timedelta(days=30)
    
    # Create the dataset
    data = []
    for i in range(n_samples):
        is_anomaly = i >= n_normal
        
        # Generate timestamp
        if is_anomaly:
            # Anomalous events are more likely to occur outside normal hours
            hour = random.choice(list(set(range(24)) - set(normal_hours)))
            minute = random.randint(0, 59)
        else:
            hour = random.choice(normal_hours)
            minute = random.randint(0, 59)
            
        timestamp = base_timestamp + timedelta(
            days=random.randint(0, 29),
            hours=hour,
            minutes=minute
        )
        
        # Select user and lock
        if is_anomaly:
            # Anomalous events might involve unusual user-lock combinations
            user_id = random.choice(user_ids)
            lock_id = random.choice(lock_ids)
        else:
            # Normal events follow more regular patterns
            user_id = random.choice(user_ids[:int(n_users * 0.8)])  # Regular users
            lock_id = random.choice(lock_ids[:int(n_locks * 0.8)])  # Commonly accessed locks
            
        # Generate access duration
        if is_anomaly:
            duration = random.uniform(10, 300)  # Unusually long or short durations
        else:
            duration = random.uniform(2, 30)    # Normal duration
            
        # Generate additional features
        access_granted = not (is_anomaly and random.random() < 0.3)
        failed_attempts = random.randint(0, 3) if is_anomaly else 0
        
        data.append({
            'timestamp': timestamp,
            'user_id': user_id,
            'lock_id': lock_id,
            'access_level': user_access_levels[user_id],
            'access_granted': access_granted,
            'access_duration': duration,
            'failed_attempts': failed_attempts,
            'day_of_week': timestamp.weekday(),
            'hour': timestamp.hour,
            'is_weekend': timestamp.weekday() >= 5,
            'is_business_hours': 8 <= timestamp.hour <= 18,
            'is_anomaly': is_anomaly
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Sort by timestamp
    df = df.sort_values('timestamp').reset_index(drop=True)
    
    # Add some derived features
    df['time_since_last_access'] = df['timestamp'].diff().dt.total_seconds()
    df['user_access_count'] = df.groupby('user_id').cumcount()
    df['lock_access_count'] = df.groupby('lock_id').cumcount()
    
    return df

if __name__ == "__main__":
    df = generate_keylock_dataset(
        n_samples=10000,
        n_locks=30,
        n_users=100,
        contamination=0.05
    )
    df.to_csv('data/synthetic_keylock_data.csv', index=False)