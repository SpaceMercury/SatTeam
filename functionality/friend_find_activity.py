import pandas as pd 

# Specify the file path
file_path = "SatTeam/data/hackupc-travelperk-dataset.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

print(df.head())