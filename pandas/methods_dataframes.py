import pandas as pandas_package

data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_full_data.csv")

dataframe_top_5_rows = data_frame_object_from_csv.head()    # Reads top 5 rows from dataframe table
dataframe_top_3_rows = data_frame_object_from_csv.head(3)   # Reads top 3 rows from dataframe table

dataframe_bottom_5_rows = data_frame_object_from_csv.tail()     # Reads bottom 5 rows from dataframe table
dataframe_bottom_3_rows = data_frame_object_from_csv.tail(3)    # Reads bottom 3 rows from dataframe table

stats_dataframe = data_frame_object_from_csv.describe()     # Return statistics of columns whose datatype is int64, float64, etc...

name_indexed_dataframe = data_frame_object_from_csv.set_index("Name")   # Set index of dataframe to specific column.
employee_17_row = name_indexed_dataframe.loc["Employee-17"]     # Look up for a row using its index
