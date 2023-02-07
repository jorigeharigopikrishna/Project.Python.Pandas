import pandas as pandas_package

# 1. Read data from csv file using pandas.read_csv() function
data_frame_object_from_csv = pandas_package.read_csv("../Datasets/employees_full_data.csv") # Assume that headers in csv file are at first row.

# 2. Read data from python dictionary using pandas.DataFrame() function
# Assume that keys are headers and values are rows in python dict.
employees_data_dict = {
    "Name": ["Emp-1", "Emp-2", "Emp-3", "Emp-4", "Emp-5"],
    "Join date": ["1/1/2023", "1/2/2023", "1/3/2023", "1/4/2023", "1/5/2023"],
    "Location": ["Bangalore", "Chennai", "Hyderabad", "Mumbai", "Noida"],
    "Role": ["Developer", "QA", "Lead", "Architect", "Manager"],
    "Skill": ["Angular", "Python", "Java", "C#", "C++"]
}
data_frame_object_from_python_dict = pandas_package.DataFrame(employees_data_dict)
