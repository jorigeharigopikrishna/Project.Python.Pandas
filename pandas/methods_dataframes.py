import pandas as pandas_package

data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_full_data.csv")

dataframe_top_5_rows = data_frame_object_from_csv.head()    # Reads top 5 rows from dataframe table
dataframe_top_3_rows = data_frame_object_from_csv.head(3)   # Reads top 3 rows from dataframe table

dataframe_bottom_5_rows = data_frame_object_from_csv.tail()     # Reads bottom 5 rows from dataframe table
dataframe_bottom_3_rows = data_frame_object_from_csv.tail(3)    # Reads bottom 3 rows from dataframe table

columns_dataframe = data_frame_object_from_csv.columns()    # Returns headers of dataframe
