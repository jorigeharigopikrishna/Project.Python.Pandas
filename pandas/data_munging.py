import pandas as pandas_package

data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_missing_data.csv", parse_dates=["Join date"], index_col="Join date", nrows=10)
print(data_frame_object_from_csv)

# 1. Using na_values parameter of pandas.read_csv() function
data_frame_object_from_csv_replace_na_values = pandas_package.read_csv("../Datasets/employees_missing_data.csv", na_values={
   "name": ["Unknown"],
   "age": [-1],
   "role": ["not available"]
})   # Replace the values of Unknown in name column, -1 in age column, not available in role column with NaN in those respective column in dataframe.

# 2. Using fillna() method of dataframe_object
df_obj_replace_all_nan_with_1 = data_frame_object_from_csv.fillna(-1)   # Replace all cells NaN values with -1
df_obj_replace_nan_based_on_column = data_frame_object_from_csv.fillna({
   "Name": "Not present",     # Name column NaN value replaced with Not present
   "Location": "India",       # Location column NaN value replaced with India
   "Role": "Unknown",         # Role column NaN value replaced with Unknown
   "Skill": "All",            # Skill column NaN value replaced with All
   "Salary": -1               # Salary column NaN value replaced with -1
})    # Replace column cells NaN values with specific value based on column.
df_obj_replace_nan_based_on_column_with_ffill = data_frame_object_from_csv.fillna(method="ffill", limit=1)   # Replace value of NaN with its previous row value in that column
df_obj_replace_nan_based_on_column_with_bfill = data_frame_object_from_csv.fillna(method="bfill", limit=1)   # Replace value of NaN with its next row value in that column
df_obj_replace_nan_based_on_column_with_previous_column = data_frame_object_from_csv.fillna(method="ffill", axis="columns")   # Replace value of NaN with its previous column value in that column
df_obj_replace_nan_based_on_column_with_next_column = data_frame_object_from_csv.fillna(method="bfill", axis="columns")   # Replace value of NaN with its next column value in that column

# 2. Using interpolate() method of dataframe_object
