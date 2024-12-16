# Electronic Keylock Access Pattern Dataset Generator

## Overview
This project contains `synth_dataset.py`, which generates realistic electronic keylock access pattern datasets for testing anomaly detection algorithms.

## Dataset Features

### Temporal Features
- **timestamp**: Date and time of access attempt
- **hour**: Hour of the day
- **day_of_week**: Day of the week
- **is_weekend**: Boolean indicating weekend access
- **is_business_hours**: Boolean indicating business hours access
- **time_since_last_access**: Time elapsed since previous access

### User/Lock Features
- **user_id**: Unique identifier for each user
- **lock_id**: Unique identifier for each lock
- **access_level**: User's access level (basic, advanced, admin)
- **user_access_count**: Cumulative count of accesses by user
- **lock_access_count**: Cumulative count of accesses for each lock

### Access Event Features
- **access_granted**: Whether access was granted
- **access_duration**: Duration of access event
- **failed_attempts**: Number of failed attempts before success

## Anomaly Patterns
The dataset includes various anomaly patterns that could indicate suspicious activity:
- Unusual access times (outside business hours)
- Unusual duration patterns
- Multiple failed attempts
- Unexpected user-lock combinations
- Access attempts from unusual users
- Weekend access patterns
- After-hours access

## Usage
You can customize the dataset generation by adjusting the following parameters:
- `n_samples`: Number of access events to generate
- `n_locks`: Number of unique locks in the system
- `n_users`: Number of unique users
- `contamination`: Proportion of anomalous events
- `random_state`: Seed for reproducibility

## Note
The anomalies are generated with different patterns from normal access events, making them suitable for anomaly detection algorithm testing. The dataset includes both temporal and behavioral patterns that could indicate suspicious activity.
