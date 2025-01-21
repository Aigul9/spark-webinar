import pandas as pd
import numpy as np

# Define the date range and campaign ID range
date_range = pd.date_range(start='2024-01-01', end='2025-01-27')
campaign_ids = range(1, 101)

# Create a list of tuples for all combinations of date and campaign_id
data = {
    "date": [],
    "campaign_id": [],
    "costs": [],
    "clicks": [],
    "views": []
}

# Generate random data for each combination
for date in date_range:
    for campaign_id in campaign_ids:
        data["date"].append(date)
        data["campaign_id"].append(campaign_id)
        data["costs"].append(round(np.random.uniform(0, 1000), 2))  # Random costs
        data["clicks"].append(np.random.randint(0, 100))            # Random clicks
        data["views"].append(np.random.randint(0, 1000))            # Random views

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("campaign_data2.csv", index=False)

print("Data saved to campaign_data.csv")
