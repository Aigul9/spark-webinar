import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Parameters
num_rows = 10000
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 1, 27)

# Generate visit IDs
visit_ids = np.random.randint(100000, 999999, num_rows)

# Generate visit date and time
visit_date_times = [start_date + timedelta(seconds=np.random.randint(0, (end_date - start_date).total_seconds())) for _ in range(num_rows)]
visit_date_times = [dt.strftime('%Y-%m-%d %H:%M:%S') for dt in visit_date_times]

# Generate URLs with different continuations
base_url = "https://our-cool-website.com/"
url_continuations = ["add", "view", "edit", "delete", "checkout", "products", "home", "contact",
                     "about", "settings", "sale", "discount", "new-arrivals", "top50", "best-sellers",
                     "featured", "reviews", "wishlist", "customer-service", "return-policy"]
urls = [base_url + np.random.choice(url_continuations) for _ in range(num_rows)]

# Generate durations
durations = np.random.randint(0, 101, num_rows)

# Generate client IDs
client_ids = np.random.randint(100, 999, num_rows)

# Generate sources
sources = np.random.choice(['ad', 'direct', 'internal', 'organic'], num_rows)

df1 = pd.read_csv('campaigns_dict.csv')

utm_campaigns = df1.iloc[:, 1].tolist()
utm_campaigns = np.random.choice(utm_campaigns, num_rows)

params = [
    ['submit', np.random.randint(1, 10000)] if np.random.rand() > 0.5 else []
    for _ in range(num_rows)
]

# Create DataFrame
data = {
    'visitid': visit_ids,
    'visitDateTime': visit_date_times,
    'URL': urls,
    'duration': durations,
    'clientID': client_ids,
    'sources': sources,
    'UTMCampaign': utm_campaigns,
    'params': params
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('visit_data.csv', index=False)
