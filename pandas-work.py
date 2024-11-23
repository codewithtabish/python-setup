# Import the pandas library
import pandas as pd

# Create a simple dataset (a list of dictionaries)
data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 35, "City": "Chicago"},
    {"Name": "David", "Age": 40, "City": "Houston"},
    {"Name": "Eva", "Age": 28, "City": "Phoenix"}
]

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# 1. Sort the DataFrame by Age in descending order
sorted_df = df.sort_values(by="Age", ascending=False)
print("\nSorted DataFrame (by Age):")
print(sorted_df)

# 2. Filter the DataFrame to show only people older than 30
filtered_df = df[df["Age"] > 30]
print("\nFiltered DataFrame (Age > 30):")
print(filtered_df)
