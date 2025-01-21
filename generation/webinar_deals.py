import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import faker

# Initialize Faker for generating random data
fake = faker.Faker()

# Parameters
num_rows = 2000

# Generate deal_id (unique IDs)
deal_ids = np.arange(1, num_rows + 1)

# Generate deal_date (random dates within a specific range)
start_date = datetime(2024, 1, 1)
end_date = datetime(2025, 1, 27)
deal_dates = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(num_rows)]
deal_dates = [date.strftime('%Y-%m-%d') for date in deal_dates]

# Generate random emails
emails = [fake.email() for _ in range(num_rows)]

# Generate random addresses
addresses = [fake.address().replace('\n', ', ') for _ in range(num_rows)]

# Generate random FIO (Full Name)
fios = [fake.name() for _ in range(num_rows)]

df1 = pd.read_csv('submit_data.csv')
phones = df1.iloc[:, 2].tolist()
phones = ['+' + str(phone) for phone in np.random.choice(phones, num_rows)]

# Generate phone numbers in the format +79019213781
# phones = [f'+79{fake.msisdn()[4:]}' for _ in range(num_rows)]

# Create DataFrame
data = {
    'deal_id': deal_ids,
    'deal_date': deal_dates,
    'fio': fios,
    'phone': phones,
    'email': emails,
    'address': addresses
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('deal_data.csv', index=False)

# Print the first few rows of the DataFrame
print(df.head())
