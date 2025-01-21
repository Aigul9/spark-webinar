import pandas as pd
import numpy as np
import faker

# Initialize Faker for generating random names and phone numbers
fake = faker.Faker()

# Parameters
num_rows = 4000

# Generate submit_id between 1 and 10000
submit_ids = np.random.randint(1, 10001, num_rows)

# Generate random names and phone numbers
names = [fake.first_name() for _ in range(num_rows)]
phones = [f'+79{fake.msisdn()[4:]}' for _ in range(num_rows)]

# Create DataFrame
data = {
    'submit_id': submit_ids,
    'name': names,
    'phone': phones
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('submit_data.csv', index=False)

# Print the first few rows of the DataFrame
print(df.head())
