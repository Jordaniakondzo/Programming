import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from joblib import dump

# Load preprocessed data
X_train = pd.read_csv('data/processed/X_train.csv')
X_test = pd.read_csv('data/processed/X_test.csv')
y_train = pd.read_csv('data/processed/y_train.csv')
y_test = pd.read_csv('data/processed/y_test.csv')

# Train the SVM model
model = SVC(kernel='linear', random_state=42)
model.fit(X_train, y_train.values.ravel())

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save the trained model
dump(model, 'trained_models/svm_model.joblib')

print("Model training and evaluation complete!")
