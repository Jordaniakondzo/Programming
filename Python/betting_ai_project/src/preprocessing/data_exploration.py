import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the fictitious dataset
df = pd.read_csv('data/raw/fictitious_data.csv')  # Adjust the path if you save the data in a different location

# Display basic statistics
print("Basic Statistics:")
print(df.describe())
print("\n")

# Count the occurrences of each bet result category
print("Distribution of Bet Results:")
print(df['BetResult'].value_counts())
print("\n")

# Check for missing values
print("Missing Values Check:")
print(df.isnull().sum())
print("\n")

# Plot the distribution of odds
plt.figure(figsize=(8, 6))
plt.hist(df['Odds'], bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribution of Odds')
plt.xlabel('Odds')
plt.ylabel('Count')
plt.show()

# Plot the distribution of recent performance
plt.figure(figsize=(8, 6))
plt.hist(df['RecentPerformance'], bins=30, edgecolor='k', alpha=0.7)
plt.title('Distribution of Recent Performance')
plt.xlabel('Performance Score')
plt.ylabel('Count')
plt.show()

# Check for correlations
correlations = df.corr()
print("Feature Correlations:")
print(correlations)
print("\n")

# Plot the correlations as a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlations, annot=True, cmap='coolwarm')
plt.title('Feature Correlations')
plt.show()
