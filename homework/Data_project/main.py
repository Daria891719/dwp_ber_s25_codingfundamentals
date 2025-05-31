import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
# After importing the file, we write the path to its in filepath
filepath = "/workspaces/dwp_ber_s25_codingfundamentals/homework/Data_project/DataAnalysisProjectData.txt"
# reading the file as a table
df = pd.read_csv(filepath)
print("Some rows of the dataframe") 
# Check of the columns and information in them (the first 2 and the last 2)
print(df.head(2))
print(df.tail(2))
print("Some information about column of the dataframe") 
# receiving some statistical information about information
print (df.describe(include="all"))
# print ("Statistical information based on given one:")
# Average salary
avg_salary = df["Salary"].mean()
print(f"Average salary: {avg_salary}")
# Average age
avg_age = df["Age"].mean()
print(f"Average age: {avg_age:.0f}")
# Experience range amongst all employees
min_experience = df["YearsOfExperience"].min()
max_experience = df["YearsOfExperience"].max()
print(f"Years of experience range is from {min_experience} to {max_experience} years")
# How many departments are there and what are these departments?
unique_departmens = df["Department"].nunique()
department_list = df["Department"].unique()
print(f"Number of departments: {unique_departmens}")
print(f"List of departments: ", department_list)

def print_mean_salary(df):
    print ("Mean salary of each department:")
    grouped = df[["Department",'Salary']].groupby(["Department"], as_index=False).mean().round(2) 
    grouped.rename(columns={'Salary': 'Mean Salary', "Department":"Department"}, inplace=True)
    print(grouped)
print_mean_salary(df)

def print_mean_quantity(df):
    print ("Quantity of people in each department:")
    grouped_quantity = df[["Department",'Name']].groupby(["Department"], as_index=False).count()
    all_employees=df['Name'].count()
    print(df["Department"])
   
    Percentage = grouped_quantity.assign(Percentage = df["Department"].count()/all_employees)
    # Percentage = grouped_quantity.assign(Percentage = grouped_quantity/all_employees)
    Percentage.rename(columns={'Name': 'Quantity', "Department":"Department"}, inplace=True)
    print(Percentage)
print_mean_quantity(df)

# import matplotlib as plt
# from matplotlib import pyplot
# plt.scatter(df["Salary"],df["Age"])
# # set x/y labels and plot title
# plt.pyplot.xlabel("Age")
# plt.pyplot.ylabel("Salary")
# plt.pyplot.title("Dependence Salary from age")
