import pandas as pandas_package

# Concat of dataframes - Supports both horizontally and vertically.
df_sheet_1 = pandas_package.read_excel("../Datasets/companies_employees_4_sheets_data.xlsx", "Infosys")
df_sheet_2 = pandas_package.read_excel("../Datasets/companies_employees_4_sheets_data.xlsx", "TCS")
df_sheet_3 = pandas_package.read_excel("../Datasets/companies_employees_4_sheets_data.xlsx", "Accenture")
df_sheet_4 = pandas_package.read_excel("../Datasets/companies_employees_4_sheets_data.xlsx", "Accenture-Role")
role_series_from_df_sheet_4 = df_sheet_4["Role"]    # Returns a Series object

# Horizontal concat where axis=0
concat_df_1_and_df_2_horizontally = pandas_package.concat([df_sheet_1, df_sheet_2])     # Concatenate / join two dataframes horizontally
concat_df_1_and_df_2_horizontally_new_index = pandas_package.concat([df_sheet_1, df_sheet_2], ignore_index=True)     # Ignore index from respective dataframes.
concat_df_1_and_df_2_horizontally_keys = pandas_package.concat([df_sheet_1, df_sheet_2], keys=["infosys", "tcs"])     # Sets the key for each dataframe in resultant concatenated dataframe.
tcs_df_after_concat = concat_df_1_and_df_2_horizontally_keys.loc["tcs"]     # Access individual dataframe from concatenated dataframe using loc[] and passing key of that dataframe.

# Vertical concat where axis=1
# 1. Concat two dataframes vertically
# concatenation won't skip common columns present in two / more dataframes / series. Common columns will appear more than once.
concat_df_3_and_df_4_vertically = pandas_package.concat([df_sheet_3, df_sheet_4], axis=1)     # Concatenate / join two dataframes vertically
print(concat_df_3_and_df_4_vertically)
# 2. Concat a dataframe and a series vertically
concat_df_and_series_vertically = pandas_package.concat([df_sheet_3, role_series_from_df_sheet_4], axis=1)     # Concatenate / join dataframe and series vertically


# Merge of dataframes - Supports only vertically.
employees_basic_dict = {
    "Name": ["Emp-1", "Emp-2", "Emp-3"],
    "Join date": ["1/1/2023", "1/2/2023", "1/3/2023"],
    "Location": ["Bangalore", "Chennai", "Hyderabad"]
}
employees_role_dict = {
    "Name": ["Emp-1", "Emp-2", "Emp-4"],
    "Role": ["Developer", "QA", "Lead"],
    "Skill": ["Angular", "Python", "All"]
}
df_employees_basic = pandas_package.DataFrame(employees_basic_dict)
df_employees_role = pandas_package.DataFrame(employees_role_dict)

# Merge two dataframes vertically on Name column as it is common for both
employees_merge_df = pandas_package.merge(df_employees_basic, df_employees_role, on="Name") # Returns the common rows as it is intersection.
employees_merge_df_inner = pandas_package.merge(df_employees_basic, df_employees_role, on="Name", how="inner") # Returns the common rows as it is intersection.

# Merge two dataframes vertically on Name column as it is common for both
employees_merge_df_outer = pandas_package.merge(df_employees_basic, df_employees_role, on="Name", how="outer") # Returns the all rows as it is union.

# Merge two dataframes vertically on Name column as it is common for both
employees_merge_df_left = pandas_package.merge(df_employees_basic, df_employees_role, on="Name", how="left")    # After merging, Return rows from left dataframe

# Merge two dataframes vertically on Name column as it is common for both
employees_merge_df_right = pandas_package.merge(df_employees_basic, df_employees_role, on="Name", how="right")    # After merging, Return rows from right dataframe

# Merge two dataframes vertically on Name column as it is common for both
# Setting an indicator such that it adds a column to tell what type of join performed on that row.
employees_merge_df_outer_indicator = pandas_package.merge(df_employees_basic, df_employees_role, on="Name", how="outer", indicator=True) # Returns the all rows as it is union.
