import pandas as pandas_package

# 1. Read data from csv file using pandas.read_csv() function
data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_full_data.csv") # Assume that headers in csv file are at first row.

# 2. Write data of dataframe to csv file using dataframe_object.to_csv() function
# Creates new csv file if not found. If found, it overrides.
data_frame_object_from_csv.to_csv("../Datasets/employees_full_data_new.csv")    # It will add index column from dataframe to csv.
data_frame_object_from_csv.to_csv("../Datasets/employees_data_new_no_index.csv", index=False)    # It will skip index column from dataframe to csv.
data_frame_object_from_csv.to_csv("../Datasets/employees_data_new_no_header.csv", header=False)    # It will skip headers row from dataframe to csv.
data_frame_object_from_csv.to_csv("../Datasets/employees_data_new_name_skill.csv", index=False, columns=["Name", "Skill"])    # It will write only name and skill columns and skip other columns from dataframe to csv.

# 3. Read data from excel file using pandas.read_excel() function.
# Since excel file will have multiple sheets, sheet name should be passed as second parameter.
# While reading excel files, make sure to install module - openpyxl installed. Otherwise it throws error.
data_frame_object_from_excel_sheet_1 = pandas_package.read_excel("../Datasets/stock_market_index_2_sheets.xlsx", "dow_jones") # Assume that headers in excel file are at first row.
data_frame_object_from_excel_sheet_2 = pandas_package.read_excel("../Datasets/stock_market_index_2_sheets.xlsx", "nasdaq") # Assume that headers in excel file are at first row.