import pandas as pd
df = pd.read_csv('Online_Cars_Sale_Marketplace.csv')
df['Price'] = pd.to_numeric(df['Price'].str.replace(r'[\$,]', '', regex=True), errors='coerce')
df = df.dropna(subset=['Price'])
df['Price'] = df['Price'].astype(int)
df['Used/New'] = df['Used/New'].replace(['Certified Pre-Owned', 'Certified Used', 'Certified'], 'Certified')
df = df[df['Drivetrain'] != '-']
df['ConsumerRating'].fillna(df['ConsumerRating'].mean(), inplace=True)
df = df.drop_duplicates()
cleaned_states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 
                'KS', 'KY', 'LA', 'MD', 'MA', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 
                'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'WA', 'WV', 'WI', 'WY']
df = df[df['State'].isin(cleaned_states)]
df.to_csv('Cleaned_Online_Cars_Sale_Marketplace.csv', index=False)
print("Data cleaning complete. Cleaned dataset saved as 'Cleaned_Online_Cars_Sale_Marketplace.csv'")

