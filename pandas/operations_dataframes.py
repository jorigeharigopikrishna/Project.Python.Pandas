import pandas as pandas_package

data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_full_data.csv")

rows_2_to_5 = data_frame_object_from_csv[2:6]   # Extract rows from 2 to 5 using slicing operation

columns_name_skill = data_frame_object_from_csv[["Name", "Skill"]]   # Extract columns - name and skill from dataframe using slicing operation

name_column_data = data_frame_object_from_csv["Name"]   # Extract column data from dataframe based on column name.
datatype_column = type(name_column_data)    # datatype of column in Series

filter_employees_salary_more_than_10 = data_frame_object_from_csv[data_frame_object_from_csv["Salary"] > 10]    # Filter the rows whose salary is more than 10
print(filter_employees_salary_more_than_10)     # Wont disturb original dataframe
