import pandas as pandas_package

# 1. Create series from dataframe. Datatype of column in dataframe is a series by default.
data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_full_data.csv")
series_salary = data_frame_object_from_csv["Salary"]  # Returns a series object
print(series_salary)

# 2. Create series from python list using pandas.Series() function
rating_list = ["Excellent", "Very Good", "Good", "Average", "Poor"]
series_object_from_python_list = pandas_package.Series(rating_list, name="Rating")
print(series_object_from_python_list)