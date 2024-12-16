
**synth_dataset.py**

This function generates a realistic electronic keylock access pattern dataset with the following features:

Temporal Features:

timestamp: Date and time of access attempt

hour: Hour of the day

day_of_week: Day of the week

is_weekend: Boolean indicating weekend access

is_business_hours: Boolean indicating business hours access

time_since_last_access: Time elapsed since previous access

User/Lock Features:

user_id: Unique identifier for each user

lock_id: Unique identifier for each lock

access_level: User's access level (basic, advanced, admin)

user_access_count: Cumulative count of accesses by user

lock_access_count: Cumulative count of accesses for each lock

Access Event Features:

access_granted: Whether access was granted

access_duration: Duration of access event

failed_attempts: Number of failed attempts before success

Anomaly Patterns:

Unusual access times (outside business hours)

Unusual duration patterns

Multiple failed attempts

Unexpected user-lock combinations

Access attempts from unusual users

Weekend access patterns

After-hours access

The anomalies are generated with different patterns from normal access events, making them suitable for anomaly detection algorithm testing. The dataset includes both temporal and behavioral patterns that could indicate suspicious activity.

You can adjust the parameters (n_samples, n_locks, n_users, contamination) to generate datasets of different sizes and characteristics. The random_state parameter ensures reproducibility of the generated data.