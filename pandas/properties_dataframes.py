import pandas as pandas_package

data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_full_data.csv")

dataframe_rows, dataframe_columns = data_frame_object_from_csv.shape
print(f"Number of rows: {dataframe_rows} and columns: {dataframe_columns}")

columns_dataframe = data_frame_object_from_csv.columns    # Returns headers of dataframe
