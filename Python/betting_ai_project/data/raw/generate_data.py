import pandas as pd
import numpy as np

# Create a random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 1000

# Generate fictitious data
data = {
    'TeamName': np.random.choice(['TeamA', 'TeamB', 'TeamC', 'TeamD'], n_samples),
    'Odds': np.random.uniform(1.5, 5.0, n_samples),
    'RecentPerformance': np.random.randint(50, 100, n_samples),
    'InjuryReports': np.random.choice([0, 1], n_samples),
    'PreviousEncountersWins': np.random.randint(0, 10, n_samples),
    'BetResult': np.random.choice(['Recommended', 'Suspect', 'Dangerous'], n_samples)
}

df = pd.DataFrame(data)

# Save the fictitious dataset to a CSV file
df.to_csv('fictitious_data.csv', index=False)

print(f"Data saved to 'fictitious_data.csv' with {n_samples} samples.")
