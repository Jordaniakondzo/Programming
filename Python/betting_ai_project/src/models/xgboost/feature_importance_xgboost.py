import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb

# Load the trained model
bst = xgb.Booster()
bst.load_model('trained_models/xgboost_model.model')

# Load the preprocessed data for feature names
X_train = pd.read_csv('data/processed/X_train.csv')

# Get feature importances
importances = bst.get_fscore()
sorted_idx = sorted(importances, key=importances.get, reverse=True)

# Plot
plt.figure(figsize=(10, 7))
plt.barh(X_train.columns, [importances[i] for i in sorted_idx])
plt.xlabel("XGBoost Feature Importance")
plt.show()
