import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

def preprocess_data(df):
    # One-Hot Encoding for TeamName
    encoder = OneHotEncoder(drop='first')
    encoded_features = encoder.fit_transform(df[['TeamName']])
    encoded_df = pd.DataFrame(encoded_features.toarray(), columns=encoder.get_feature_names_out(['TeamName']))
    df = pd.concat([df, encoded_df], axis=1)
    df = df.drop(['TeamName'], axis=1)

    # Split data into training and test sets
    X = df.drop('BetResult', axis=1)
    y = df['BetResult']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    df = pd.read_csv('data/raw/fictitious_data.csv')
    X_train, X_test, y_train, y_test = preprocess_data(df)
    print("Data preprocessing is complete!")

    # Save the preprocessed data
    X_train.to_csv('data/processed/X_train.csv', index=False)
    X_test.to_csv('data/processed/X_test.csv', index=False)
    y_train.to_csv('data/processed/y_train.csv', index=False)
    y_test.to_csv('data/processed/y_test.csv', index=False)
