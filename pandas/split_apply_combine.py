import pandas as pandas_package

df_object = pandas_package.read_csv("../Datasets/weather_data_groups.csv", parse_dates=["Date"])

# Groupby() function of dataframe groups dataframe by a specific column.
# Also called as SPLIT-APPLY-COMBINE process.
# It returns DataFrameGroupBy object which is a dictionary of key-value pairs where key is group name and value is a dataframe for that group.

# SPLIT OPERATION where it splits dataframe into groups
df_object_group_city = df_object.groupby("Location")    # Grouping dataframe by Location column.

# APPLY & COMBINE where it applies some operations on each dataframe and combines its results into a single dataframe.
df_with_max_values = df_object_group_city.max()     # Applying max() operation on individual groups and Combine them into a dataframe.

df_with_min_values = df_object_group_city.min()     # Applying min() operation on individual groups and Combine them into a dataframe.

# Mean works only with columns of datatype - int64, float64
df_with_mean_values = df_object_group_city.mean()     # Applying mean() operation on individual groups and Combine them into a dataframe.

df_with_group_stats = df_object_group_city.describe()     # Applying describe() operation on individual groups to get its statistics and Combine them into a dataframe.

for city, city_data_frame in df_object_group_city:  # Use of for() loop to iterate through dictionary.
    print(city)
    print(city_data_frame)

noida_df = df_object_group_city.get_group("Noida")  # To get the dataframe of individual group using its group_name.
