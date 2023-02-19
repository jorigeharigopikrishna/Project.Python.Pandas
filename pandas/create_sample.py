import pandas as pandas_package

df_object = pandas_package.read_csv("../Datasets/employees_full_data.csv")

sample_15_object = df_object.sample(15)     # Create sample of 15 data points
print(sample_15_object)
