import pandas as pandas_package

df_object = pandas_package.read_csv("../Datasets/employees_full_data.csv")

sample_50_object = df_object.sample(50)     # Create sample of 50 data points
