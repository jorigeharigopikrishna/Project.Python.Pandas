import pandas as pandas_package

df_object = pandas_package.read_csv("../Datasets/weather_data_groups.csv")
df_object_2 = pandas_package.read_csv("../Datasets/weather_data_groups_mrng_evng.csv")
df_object_3 = pandas_package.read_csv("../Datasets/weather_data_grouper_months.csv", parse_dates=["Date"])

# Pivot is used to transform or reshape dataframe.
# Using dataframe_object.pivot() method
pivot_df = df_object.pivot(index="Date", columns="Location")    # Setting Date column as row values and Location column as column values and other columns as values of dataframe.

pivot_df_2 = df_object.pivot(index="Location", columns="Date")  # Setting Location column as row values and Date column as column values and other columns as values of dataframe.

pivot_df_2_temp = df_object.pivot(index="Location", columns="Date", values="Temperature")   # Setting Location column as row values and Date column as column values and only include temperature column as values of dataframe.

pivot_df_2_windspeed = df_object.pivot(index="Location", columns="Date", values="Windspeed")       # Setting Location column as row values and Date column as column values and only include windspeed column as values of dataframe.

pivot_df_2_event = df_object.pivot(index="Location", columns="Date", values="Event")       # Setting Location column as row values and Date column as column values and only include event column as values of dataframe.

# Pivot_table is used to aggregate and summarize data inside dataframe.
# Using dataframe_object.pivot_table() method
# Since it aggregates data by performing some calculations, it works only with columns of datatypes – int4, float64
pivot_table_df_mean = df_object_2.pivot_table(index="Date", columns="Location")  # Aggregates data by mean()

pivot_table_df_sum = df_object_2.pivot_table(index="Date", columns="Location", aggfunc="sum")  # Aggregates data by sum()

pivot_table_df_std = df_object_2.pivot_table(index="Date", columns="Location", aggfunc="std")  # Aggregates data by std()

# Pivot table grouper to aggregate data inside dataframe based on frequency.
# freq="M" returns last working day (28 / 30 / 31) of that month
pivot_table_grouper_monthly = df_object_3.pivot_table(index=pandas_package.Grouper(freq="M", key="Date"), columns="Location")   # Aggreates data on monthly basis by mean()
# freq="W" returns sunday of that week
pivot_table_grouper_weekly = df_object_3.pivot_table(index=pandas_package.Grouper(freq="W", key="Date"), columns="Location")   # Aggreates data on weekly basis by mean()
