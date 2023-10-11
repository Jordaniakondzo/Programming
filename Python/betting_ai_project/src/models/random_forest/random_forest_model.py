import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.utils.class_weight import compute_class_weight
from joblib import dump

# Load preprocessed data
X_train = pd.read_csv('data/processed/X_train.csv')
X_test = pd.read_csv('data/processed/X_test.csv')
y_train = pd.read_csv('data/processed/y_train.csv')
y_test = pd.read_csv('data/processed/y_test.csv')

# Extract unique labels from y_train and convert to integers
unique_labels = y_train['BetResult'].unique()
label_to_int = {label: idx for idx, label in enumerate(unique_labels)}

# Convert labels to integers for training
y_train_int = y_train['BetResult'].map(label_to_int)
y_test_int = y_test['BetResult'].map(label_to_int)

# Calculate class weights
class_weights = compute_class_weight('balanced', classes=list(label_to_int.values()), y=y_train_int)
weights_dict = {int_val: weight for int_val, weight in zip(label_to_int.values(), class_weights)}

# Train the random forest model with class weights
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight=weights_dict)
model.fit(X_train, y_train_int)

# Predict on test set
y_pred = model.predict(X_test)

# Convert integer predictions back to original labels
y_pred_labels = [unique_labels[int_val] for int_val in y_pred]

# Evaluate the model
accuracy = accuracy_score(y_test_int, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test_int, y_pred, target_names=unique_labels))

# Save the trained model
dump(model, 'trained_models/random_forest_model.joblib')

print("Model training and evaluation complete!")
