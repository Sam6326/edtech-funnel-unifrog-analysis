import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('edtech_student_funnel.csv')
print("Data loaded successfully. Shape:", df.shape)

df['is_mobile'] = (df['device'] == 'Mobile').astype(int)
df['engagement_index'] = df['prior_engagement_score'] * df['sessions_count'] / 100

student_df = df.drop_duplicates(subset=['student_id']).copy()

features = ['age', 'prior_engagement_score', 'sessions_count', 'avg_session_duration_min', 'is_mobile', 'school_type', 'gender']
X = student_df[features]
y = student_df['completed_application']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['age', 'prior_engagement_score', 'sessions_count', 'avg_session_duration_min']),
        ('cat', OneHotEncoder(drop='first', handle_unknown='ignore'), ['school_type', 'gender'])
    ])

model = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

print("\nModel Performance:")
print(classification_report(y_test, y_pred))
print(f"AUC-ROC: {roc_auc_score(y_test, y_proba):.3f}")

coefs = model.named_steps['classifier'].coef_[0]
feature_names = list(model.named_steps['preprocessor'].named_transformers_['num'].get_feature_names_out()) + list(model.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out())
importance = pd.DataFrame({'feature': feature_names, 'coef': coefs}).sort_values('coef', ascending=False)
print("\nTop Predictors:\n", importance.head(10))

plt.figure(figsize=(10,6))
sns.barplot(data=importance.head(8), x='coef', y='feature')
plt.title('Top Predictors of Application Completion')
plt.tight_layout()
plt.savefig('feature_importance.png')
print("Plot saved: feature_importance.png")
