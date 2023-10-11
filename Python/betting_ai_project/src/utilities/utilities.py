import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

LOG_FILE_PATH = "project_log.txt"

def load_data(path):
    return pd.read_csv(path)

def save_data(df, path):
    df.to_csv(path, index=False)

def plot_confusion_matrix(y_true, y_pred, classes):
    matrix = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(10,7))
    sns.heatmap(matrix, annot=True, cmap='Blues', fmt='g',
               xticklabels=classes,
               yticklabels=classes)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

def calculate_metrics(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='macro')
    recall = recall_score(y_true, y_pred, average='macro')
    f1 = f1_score(y_true, y_pred, average='macro')
    return accuracy, precision, recall, f1

def log(message, file=LOG_FILE_PATH):
    """
    Utility function to log a message to console and to a file.
    """
    print(message)
    with open(file, 'a') as log_file:
        log_file.write(str(message) + "\n")
