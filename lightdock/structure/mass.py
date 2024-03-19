import pandas as pd

# Read the Excel file into a DataFrame
mass_df = pd.read_excel('mass.xlsx')

# Convert DataFrame to dictionary
mass_dict = mass_df.set_index('element')['mass'].to_dict()
