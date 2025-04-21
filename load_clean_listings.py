import pandas as pd

# Load listings dataset
listings = pd.read_csv("listings.csv")

# Clean price column by removing dollar signs and commas, and convert to float
listings['price'] = listings['price'].replace('[\$,]', '', regex=True).astype(float)

# Drop rows with NaN values in 'neighbourhood' and 'price'
listings = listings.dropna(subset=['neighbourhood', 'price'])

# Display the cleaned data
print(listings.head())
