import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def reading (filepath): 
    # reading the file as a table
    df = pd.read_csv(filepath)
    print("Some rows of the dataframe") 
    #  Check of the columns and information in them (the first 2 and the last 2)
    print(df.head(2))
    print(df.tail(2))
    return df
filepath = "/workspaces/dwp_ber_s25_codingfundamentals/homework/Data_project/DataAnalysisProjectData.txt"
df= reading (filepath)
print("Some information about column of the dataframe") 
# receiving some statistical information about information
print (df.describe(include="all"))

print ("Statistical information based on given one:")
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
    quantity = df.groupby(["Department"]).count()["Name"]
    quantity_columns = quantity.to_frame(name="Precentage").reset_index()
    quantity_columns["Precentage"] = quantity_columns["Precentage"] / quantity_columns["Precentage"].sum()*100
    # grouped_quantity_columns.rename(columns={'Percentage': 'Percentage', "Department":"Department"}, inplace=True)
    # quantity_department={}
    # for department in range(0,len (department_list)):
    #     quantity_department[department]=df["Name"].count
    # print(quantity_department) 
    print(quantity_columns)
    return quantity_columns
quantity=print_mean_quantity(df)
def pie_chart (massiv):
    y = np.array(quantity["Precentage"])
    labels = quantity["Department"]
    plt.pie(y, labels=labels, autopct='%1.1f%%')
    plt.show()
pie_chart(quantity)
