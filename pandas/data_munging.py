import pandas as pandas_package

# 1. Using na_values parameter of pandas.read_csv() function
data_frame_object_from_csv_replace_na_values = pandas_package.read_csv("../Datasets/employees_missing_data.csv", na_values={
   "name": ["Unknown"],
   "age": [-1],
   "role": ["not available"]
})   # Replace the values of Unknown in name column, -1 in age column, not available in role column with NaN in those respective column in dataframe.
