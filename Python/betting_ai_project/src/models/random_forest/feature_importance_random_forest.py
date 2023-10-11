import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from joblib import load

# Load the trained model
model = load('trained_models/random_forest_model.joblib')

# Load the preprocessed data for feature names
X_train = pd.read_csv('data/processed/X_train.csv')

# Get feature importances
importances = model.feature_importances_
sorted_idx = importances.argsort()

# Plot
plt.figure(figsize=(10, 7))
plt.barh(X_train.columns[sorted_idx], importances[sorted_idx])
plt.xlabel("Random Forest Feature Importance")
plt.show()
