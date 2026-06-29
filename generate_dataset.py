import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid

np.random.seed(42)
n_students = 5000

# Base students
students = pd.DataFrame({
    'student_id': [str(uuid.uuid4())[:8] for _ in range(n_students)],
    'age': np.random.randint(14, 19, n_students),
    'gender': np.random.choice(['M', 'F'], n_students),
    'school_type': np.random.choice(['State', 'Private'], n_students, p=[0.7, 0.3]),
    'device': np.random.choice(['Mobile', 'Desktop'], n_students, p=[0.6, 0.4]),
    'prior_engagement_score': np.random.normal(60, 15, n_students).clip(10, 100),
    'sessions_count': np.random.poisson(10, n_students),
    'avg_session_duration_min': np.random.normal(15, 8, n_students).clip(2, 60),
})

# Strong target correlation
logit = -3 + 0.08 * students['prior_engagement_score'] + 0.12 * students['sessions_count'] + 0.09 * students['avg_session_duration_min'] - 1.2 * (students['device'] == 'Mobile')
prob = 1 / (1 + np.exp(-logit))
students['completed_application'] = (np.random.rand(n_students) < prob).astype(int)

# Generate events (simplified for speed)
stages = ['Login', 'Browse_Courses', 'View_Details', 'Start_Application', 'Complete_Application']
events = []
for _, s in students.iterrows():
    if s['completed_application'] == 1:
        for stage in stages:
            events.append({'student_id': s['student_id'], 'stage': stage, 'timestamp': datetime(2025,1,1), 'duration_sec': 100, 'success': 1})
    else:
        for stage in stages[:3]:  # Drop early
            events.append({'student_id': s['student_id'], 'stage': stage, 'timestamp': datetime(2025,1,1), 'duration_sec': 100, 'success': 1})

events_df = pd.DataFrame(events)
full_df = events_df.merge(students, on='student_id')
full_df.to_csv('edtech_student_funnel.csv', index=False)

print('SUCCESS: Stronger dataset created')
print('Completion rate:', students['completed_application'].mean())
