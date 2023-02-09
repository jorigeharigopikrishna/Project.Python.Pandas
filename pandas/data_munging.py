import pandas as pandas_package
import numpy as numpy_package

data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_missing_data.csv", parse_dates=["Join date"], index_col="Join date", nrows=10)  # Get top 10 rows
print(data_frame_object_from_csv)
data_frame_object_from_csv_invalid_data = pandas_package.read_csv("../Datasets/employees_invalid_data.csv", parse_dates=["Join date"], index_col="Join date", nrows=10)    # Get top 10 rows
print(data_frame_object_from_csv_invalid_data)
dataframe_dict = pandas_package.DataFrame({
    "score": ["good", "avg", "excellent"],
    "student": ["Ab", "Bc", "Cd"]
})
print(dataframe_dict)

# 1. Using na_values parameter of pandas.read_csv() function
data_frame_object_from_csv_replace_na_values = pandas_package.read_csv("../Datasets/employees_missing_data.csv", na_values={
   "name": ["Unknown"],
   "age": [-1],
   "role": ["not available"]
})   # Replace the values of Unknown in name column, -1 in age column, not available in role column with NaN in those respective column in dataframe.

# 2. Using fillna() method of dataframe_object
# It deals with only NaN values
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

# 3. Using interpolate() method of dataframe_object which performs linear interpolation.
# Replace NaN values with guesses based on method parameter between previous cell value and next cell value.
# Note that, it works only with columns of datatype - int64, float64. Other column values of NaN remains same.
df_obj_replace_nan_with_interpolate_values = data_frame_object_from_csv.interpolate()  # Default value of method parameter is linear. Equally spaced values. Replace salary column only as it is integer datatype.
df_obj_replace_nan_with_linear_interpolate_values = data_frame_object_from_csv.interpolate(method="linear")  # Equally spaced values. Replace salary column only as it is integer datatype.
df_obj_replace_nan_with_time_interpolate_values = data_frame_object_from_csv.interpolate(method="time")  # Guess values based on date / time. Replace salary column only as it is integer datatype.

# 4. Using dropna() method of dataframe_object which is used to drop / not-include rows into the dataframe.
# Dropping / Not-including of rows based on how / thresh parameter.
df_obj_drop_rows_any_one_na_value = data_frame_object_from_csv.dropna()  # Drop rows if any of its of columns has NaN value.
df_obj_drop_rows_all_has_na_values = data_frame_object_from_csv.dropna(how="all")  # Drop rows if all of columns in that row has NaN value.
df_obj_drop_rows_less_than_2_non_nan_values = data_frame_object_from_csv.dropna(thresh=2)  # Drop rows if that row has less than 2 NaN values.

# 5. Using reindex() method of dataframe_object to insert missing rows into teh dataframe based on index.
# Values of columns of such rows which are added will have NaN values by default.
# It wont disturb original dataframe.
start_date = data_frame_object_from_csv.index[0]   # Get start index at 0
end_date = data_frame_object_from_csv.index[-1]    # Get last index at -1
date_range = pandas_package.date_range(start_date, end_date)   # Create dates range object
updated_index = pandas_package.DatetimeIndex(date_range)       # Convert dates range object to date time index
data_frame_object_with_missing_rows_added = data_frame_object_from_csv.reindex(updated_index)   # reindex() method will rearrange index of dataframe and returns new dataframe.

# 6. Using replace() method of dataframe_object
# It does not deal with NaN values. It deals with non-NaN values.
df_obj_replace_all_1_with_nan_value = data_frame_object_from_csv_invalid_data.replace(-1, numpy_package.NaN)   # Replace all cells non-NaN values of -1 with NaN
df_obj_replace_more_than_non_nan_with_nan_value = data_frame_object_from_csv_invalid_data.replace(["No name", -1, "Unknown"], numpy_package.NaN)   # Replace all cells non-NaN values of No name, -1, Unknown with NaN
df_obj_replace_more_than_non_nan_with_its_own_value = data_frame_object_from_csv_invalid_data.replace({
    "No name": numpy_package.NaN,     # No name value replaced with NaN
    -1: 0               # -1 value replaced with 0
 })    # Replace No name with NaN and -1  with 0 across all cells.
df_obj_replace_non_nan_based_on_column_with_nan_value = data_frame_object_from_csv_invalid_data.replace({
    "Name": "No name",     # Name column No name value replaced with NaN
    "Role": "Unknown",         # Role column Unknown value replaced with NaN
    "Salary": -1               # Salary column -1 value replaced with NaN
}, numpy_package.NaN)    # Replace column cells non-NaN values with specific value based on column.
df_obj_replace_all_regex_match_with_empty_str = data_frame_object_from_csv_invalid_data.replace("a-zA-Z0-9", "", regex=True)   # Replace all cells values which match given regex pattern with ""
df_obj_replace_all_regex_match_based_on_column_with_empty_str = data_frame_object_from_csv_invalid_data.replace({
    "Name": "a-zA-Z0-9",     # Name column value match given regex pattern replaced with ""
    "Role": "a-zA-Z0-9",         # Role column value match given regex pattern replaced with ""
}, "", regex=True)    # Replace column cells non-NaN values which matches given regex pattern with "" based on column.
dataframe_dict_replace = dataframe_dict.replace(["good", "avg", "excellent"], [1, 2, 3])    # Replace list with another list
