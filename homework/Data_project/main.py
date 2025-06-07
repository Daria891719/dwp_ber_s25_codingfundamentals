import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def reading (filepath):
    df = pd.read_csv(filepath)
    print("Some rows of the dataframe")
    #  Check of the columns and information in them (the first 2 and the last 2)
    print(df.head(2))
    print(df.tail(2))
    print("Some information about column of the dataframe")
    # Receiving some statistical information about information
    print (df.describe(include="all"))
filepath = "/workspaces/dwp_ber_s25_codingfundamentals/homework/Data_project/DataAnalysisProjectData.txt"
df = reading (filepath)
# Average salary
avg_salary = df["Salary"].mean()
# Average age
avg_age = df["Age"].mean()
# Experience range amongst all employees
min_experience = df["YearsOfExperience"].min()
max_experience = df["YearsOfExperience"].max()
# How many departments are there and what are these departments?
unique_departments = df["Department"].nunique()
department_list = ", ".join(map(str, df["Department"].unique()))
data = [
    ["Average salary", f"{avg_salary:.2f}"],
    ["Average age", f"{avg_age:.0f}"],
    ["Experience range", f"{min_experience} - {max_experience} years"],
    ["Number of departments", str(unique_departments)],
    ["List of departments", department_list]
]
print ("Statistical information based on given one:")
print("-" * 78)
print(f"{'| Parameter':<35} | {'Value':<40}|")
print("-" * 78)
for row in data:
    parameter, value = row
    print(f"| {parameter:<33} | {value:<40}|")
print("-" * 78)
def print_mean_salary(df):
    print ("Mean salary of each department:")
    grouped = df[["Department","Salary"]].groupby(["Department"], as_index=False).mean().round(2)
    grouped.rename(columns={"Salary": "Mean Salary"}, inplace=True)
    print(grouped)
    return grouped
def bar_mean_salary(df):
    grouped = print_mean_salary(df)
    plt.bar(grouped["Department"], grouped["Mean Salary"])
    plt.xlabel("Department")
    plt.ylabel("Mean Salary")
    plt.title("Mean Salary by Department")
    plt.savefig("department_mean_salary.png")  # Save the bar chart
    plt.show()
bar_mean_salary(df)
def print_mean_quantity(df):
    print ("Quantity of people in each department:")
    quantity = df.groupby(["Department"]).count()["Name"]
    quantity_columns = quantity.to_frame(name="Share (%)").reset_index()
    quantity_columns["Share (%)"] = quantity_columns["Share (%)"] / quantity_columns["Share (%)"].sum()*100
    # grouped_quantity_columns.rename(columns={'Percentage': 'Percentage', "Department":"Department"}, inplace=True)
    # quantity_department={}
    # for department in range(0,len (department_list)):
    #     quantity_department[department]=df["Name"].count
    # print(quantity_department)
    print(quantity_columns)
    return quantity_columns
quantity_df=print_mean_quantity(df)
def pie_chart (massiv):
    y = massiv["Share (%)"].values
    labels = massiv["Department"].values
    plt.pie(y, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')  # Makes the pie chart round
    plt.title ("Quantity of people in each department")
    plt.savefig("department_pie_chart.png")  # Save the pie chart
    plt.show()
pie_chart(quantity_df)