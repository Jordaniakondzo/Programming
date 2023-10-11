import sys
sys.path.append('..')

import joblib
from src.preprocessing.data_preprocessing import preprocess_data
from src.utilities.utilities import load_data, plot_confusion_matrix, calculate_metrics, log 

def main():
    log("=== Starting Betting AI Project Execution ===")
    
    # 1. Load raw data
    log("Loading raw data...")
    raw_data = load_data('data/raw/fictitious_data.csv')
    
    # 2. Preprocess data
    log("Preprocessing data...")
    X_train, X_test, y_train, y_test = preprocess_data(raw_data)
    
    # 3. Evaluate Models
    
    # Logistic Regression Model
    logistic_model = joblib.load('trained_models/logistic_model.joblib')
    log("Evaluating Logistic Regression Model...")
    evaluate_model(logistic_model, X_test, y_test, "Logistic Regression")
    
    # Random Forest Model
    rf_model = joblib.load('trained_models/random_forest_model.joblib')
    log("Evaluating Random Forest Model...")
    evaluate_model(rf_model, X_test, y_test, "Random Forest")

    # XGBoost Model
    xgb_model = joblib.load('trained_models/xgboost_model.model')
    log("Evaluating XGBoost Model...")
    evaluate_model(xgb_model, X_test, y_test, "XGBoost")

    # Decision Tree Model
    dt_model = joblib.load('trained_models/decision_tree_model.joblib')
    log("Evaluating Decision Tree Model...")
    evaluate_model(dt_model, X_test, y_test, "Decision Tree")

    # SVM Model
    svm_model = joblib.load('trained_models/svm_model.joblib')
    log("Evaluating SVM Model...")
    evaluate_model(svm_model, X_test, y_test, "SVM")
    
    log("=== Betting AI Project Execution Finished ===")


def evaluate_model(model, X_test, y_test, model_name):
    """
    Helper function to evaluate a model using test data and print results.
    """
    y_pred = model.predict(X_test)
    log(f"Evaluation results for {model_name}:")
    log(calculate_metrics(y_test, y_pred))  # Assuming `calculate_metrics` returns a string representation of evaluation metrics.


if __name__ == "__main__":
    main()
