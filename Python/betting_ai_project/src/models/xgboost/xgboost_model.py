import pandas as pd
import xgboost as xgb
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
from joblib import dump

# Load preprocessed data
X_train = pd.read_csv('data/processed/X_train.csv')
X_test = pd.read_csv('data/processed/X_test.csv')
y_train = pd.read_csv('data/processed/y_train.csv')
y_test = pd.read_csv('data/processed/y_test.csv')

# Convert labels to integers using LabelEncoder
encoder = LabelEncoder()
y_train_encoded = encoder.fit_transform(y_train.values.ravel())
y_test_encoded = encoder.transform(y_test.values.ravel())

# Parameter grid for GridSearchCV
param_grid = {
    'objective': ['multi:softmax'],
    'learning_rate': [0.01, 0.1, 0.5],
    'max_depth': [3, 5, 7],
    'colsample_bytree': [0.5, 0.7, 1],
    'n_estimators': [50, 100, 150]
}

model = xgb.XGBClassifier(random_state=42)
grid_search = GridSearchCV(model, param_grid, cv=3, verbose=1)
grid_search.fit(X_train, y_train_encoded)

# Best model from grid search
best_xgb = grid_search.best_estimator_

# Predict on test set
y_pred = best_xgb.predict(X_test)

# Convert integer predictions back to original labels
y_pred_labels = encoder.inverse_transform(y_pred.astype(int))

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred_labels)
print(f"Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_labels))

# Save the trained model
best_xgb.save_model('trained_models/xgboost_model.model')

print("Model training and evaluation complete!")
