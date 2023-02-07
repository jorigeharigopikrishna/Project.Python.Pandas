import pandas as pandas_package

# 1. Create series from dataframe. Datatype of column in dataframe is a series by default.
data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_full_data.csv")
series_salary = data_frame_object_from_csv["Salary (LPA)"]  # Returns a series object
print(series_salary)
