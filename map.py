import os
import pandas as pd

# Define the directory containing the CSV files
directory = "."

# Initialize a dictionary to store the dataframes
dataframes = {}

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        # Read the CSV file into a dataframe
        df = pd.read_csv(os.path.join(directory, filename))
        # Use the first column as the index (assuming it's the ID column)
        df.set_index(df.columns[0], inplace=True)
        # Store the dataframe in the dictionary
        dataframes[filename] = df

# Concatenate all dataframes into a single dataframe
merged_df = pd.concat(dataframes.values(), keys=dataframes.keys())

# Write the merged dataframe to a new CSV file
output_file = "merged_data.csv"
merged_df.to_csv(output_file)

print(f"Dataframes have been written to {output_file}")