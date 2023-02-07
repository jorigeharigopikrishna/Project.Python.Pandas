import pandas as pandas_package

data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_full_data.csv")
series_salary = data_frame_object_from_csv["Salary (LPA)"]  # Returns a series object

max_salary = series_salary.max()    # Maximum value of the series
min_salary = series_salary.min()    # Minimum value of the series
mean_salary = series_salary.mean()      # Mean or Average value of the series
std_salary = series_salary.std()    # Standard deviation value of the series
