import matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
matplotlib.use('Agg')  # Set non-interactive backend
import matplotlib.pyplot as plt
from dataset import preprocess_dataset, load_voice_dataset

# Load raw dataset and extract target
raw_df = load_voice_dataset().drop(columns=["Unnamed: 0", "index"], errors="ignore")
y = raw_df["status"]

# Drop target and any non-feature columns, then preprocess
feature_df = raw_df.drop(columns=["status", "name"], errors="ignore")

X = preprocess_dataset(feature_df)
# Align target vector with features after outlier removal
y = y.loc[X.index]

# Handle missing values for numeric columns only
X = X.fillna(X.mean())

# Rest of your code remains the same
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize Random Forest
rf = RandomForestClassifier(random_state=42)

# Hyperparameter tuning
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 15, 20],
    'min_samples_split': [2, 5]
}
grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='f1')
grid_search.fit(X_train, y_train)

# Best model
best_rf = grid_search.best_estimator_

# Save the trained model for later use
import joblib
joblib.dump(best_rf, 'src/artifacts/model.joblib')

# Predictions
y_pred = best_rf.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.savefig('src/artifacts/confusion_matrix.png')
plt.close()

# Feature Importance
feature_importance = pd.Series(best_rf.feature_importances_, index=X.columns)
feature_importance.nlargest(10).plot(kind='barh')
plt.title('Top 10 Feature Importance')
plt.tight_layout()
plt.savefig('src/artifacts/feature_importance.png')
plt.close()
