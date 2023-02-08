import pandas as pandas_package

# 1. Read data from csv file using pandas.read_csv() function
data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_full_data.csv") # Assume that headers in csv file are at first row.
data_frame_object_from_csv_skiprows_2 = pandas_package.read_csv("../Datasets/employees_full_data_headers_2.csv", skiprows=1) # Assume that headers in csv file are at second row.
data_frame_object_from_csv_headers_2 = pandas_package.read_csv("../Datasets/employees_full_data_headers_2.csv", header=1) # Assume that headers in csv file are at second row.
data_frame_object_from_csv_rows_4 = pandas_package.read_csv("../Datasets/employees_full_data.csv", nrows=4) # Return top 4 rows.
data_frame_object_from_csv_replace_na_values = pandas_package.read_csv("../Datasets/employees_missing_data.csv", na_values={
   "name": ["Unknown"],
   "age": [-1],
   "role": ["not available"]
})   # Replace the values of Unknown in name column, -1 in age column, not available in role column with NaN in those respective column in dataframe.
data_frame_object_from_csv_parse_dates_columns_from_str_to_datetime = pandas_package.read_csv("../Datasets/employees_full_data.csv", parse_dates=["Join date"])     # Converts datatype of Join date column values to timestamp datatype.
data_frame_object_from_csv_date_index = pandas_package.read_csv("../Datasets/employees_full_data.csv", index_col="Join date")     # Sets Join date as index of dataframe.

# 2. Read data from excel file using pandas.read_excel() function.
# Since excel file will have multiple sheets, sheet name should be passed as second parameter.
# While reading excel files, make sure to install module - openpyxl installed. Otherwise it throws error.
data_frame_object_from_excel_sheet_1 = pandas_package.read_excel("../Datasets/stock_market_index_2_sheets.xlsx", "dow_jones") # Assume that headers in excel file are at first row.
data_frame_object_from_excel_sheet_2 = pandas_package.read_excel("../Datasets/stock_market_index_2_sheets.xlsx", "nasdaq") # Assume that headers in excel file are at first row.

# 3. Read data from python dictionary using pandas.DataFrame() function
# Assume that keys are headers and values are rows in python dict.
employees_data_dict = {
    "Name": ["Emp-1", "Emp-2", "Emp-3", "Emp-4", "Emp-5"],
    "Join date": ["1/1/2023", "1/2/2023", "1/3/2023", "1/4/2023", "1/5/2023"],
    "Location": ["Bangalore", "Chennai", "Hyderabad", "Mumbai", "Noida"],
    "Role": ["Developer", "QA", "Lead", "Architect", "Manager"],
    "Skill": ["Angular", "Python", "Java", "C#", "C++"]
}
data_frame_object_from_python_dict = pandas_package.DataFrame(employees_data_dict)

# 4. Read data from python list of tuples using pandas.DataFrame() function
# Column headers needs to be passed as second parameter and rows to be passed as list of tuples.
employees_data_list_of_tuples = [
    ("Emp-1", "1/1/2023", "Bangalore", "Developer", "Angular"),
    ("Emp-2", "1/2/2023", "Chennai", "QA", "Python"),
    ("Emp-3", "1/3/2023", "Hyderabad", "Lead", "Java"),
    ("Emp-4", "1/4/2023", "Mumbai", "Architect", "C#"),
    ("Emp-5", "1/5/2023", "Noida", "Manager", "C++")
]
data_frame_object_from_python_list_of_tuples = pandas_package.DataFrame(employees_data_list_of_tuples, columns=["Name", "Date", "Location", "Role", "Skill"])

# 5. Read data from python list of dictionaries using pandas.DataFrame() function
# Note that key across all dictionary objects are same and they become headers and values of keys will become cells of rows.
employees_data_list_of_dicts = [
    {"name": "Emp-1", "date": "1/1/2023", "role": "Developer"},
    {"name": "Emp-2", "date": "1/2/2023", "role": "QA"},
    {"name": "Emp-3", "date": "1/3/2023", "role": "Lead"}
]
data_frame_object_from_python_list_of_dicts = pandas_package.DataFrame(employees_data_list_of_dicts)
