import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def reading (filepath): 
    df = pd.read_csv(filepath)
    print("Some rows of the dataframe") 
    #  Check of the columns and information in them (the first 2 and the last 2)
    print(df.head(2))
    print(df.tail(2))
    print("Summary statistics of the columns. This is a standard function for analyzing the imported data.") 
    print (df.describe(include="all"))
    return df
filepath = "/workspaces/dwp_ber_s25_codingfundamentals/homework/Data_project/DataAnalysisProjectData.txt"
df= reading (filepath)

def statistics(df):
    avg_salary = df["Salary"].mean()
    # Average age
    avg_age = df["Age"].mean()
    # Experience range among all employees
    min_experience = df["YearsOfExperience"].min()
    max_experience = df["YearsOfExperience"].max()
    # How many departments are there and what are these departments?
    unique_departments = df["Department"].nunique()
    department_list = ", ".join(map(str, df["Department"].unique()))
    data = [
        ["Average salary", f"{avg_salary:.2f}"],
        ["Average age", f"{avg_age:.0f}"],
        ["Years of experience range", f"{min_experience} - {max_experience} years"],
        ["Number of departments", str(unique_departments)],
        ["List of departments", department_list]
    ]
    return data
data=statistics(df) 
# Display summary table with calculated statistics
def print_data(data): 
    print ("Statistical information based on given data:")
    print("-" * 78)
    print(f"{'| Parameter':<35} | {'Value':<40}|")
    print("-" * 78)
    for row in data:
        parameter, value = row
        print(f"| {parameter:<33} | {value:<40}|")
    print("-" * 78)
    return None
statistic = print_data(data)

def print_mean_salary(df):
    print ("Mean salary of each department:")
    grouped = df[["Department","Salary"]].groupby(["Department"], as_index=False).mean().round(2)  
    grouped.rename(columns={"Salary": "Mean Salary"}, inplace=True)
    return grouped 
mean_salary=print_mean_salary(df)
print (mean_salary)
def bar_mean_salary(df):
    grouped = print_mean_salary(df)
    plt.bar(grouped["Department"], grouped["Mean Salary"])
    plt.xlabel("Department")
    plt.ylabel("Mean Salary")
    plt.title("Mean Salary by Department")
    plt.savefig("department_mean_salary.png")  # Save the bar chart
    plt.show()
bar_mean_salary_plot=bar_mean_salary(df)

def dependence (df):
    print ("Dependence salary from age:")
    df_age_salary=df[["Department","Salary", "Age"]] # Create a new DataFrame with relevant columns
    bins=np.linspace(df_age_salary["Age"].min(),df_age_salary["Age"].max(), 5) #  Divide the age into 4 equal-width categories using the min and max values (5 edges = 4 bins)
    group_names = ["20-30","30-40", "40-50", "50-60"] # Define labels for the age groups
    df["Age group"]=pd.cut(df["Age"], bins=bins, labels= group_names, include_lowest=True) # Categorize the "Age" column into the defined age groups
    grouped = df.groupby(["Department","Age group"], as_index=False)["Salary"].mean().round(2) 
    df_pivot= grouped.pivot(index= "Department", columns="Age group", values="Salary") # Pivot the table to show average salary by department and age group
    print(df_pivot)
    return df_pivot 
dependence_age_salary=dependence (df)
# According to the data, there is no visible correlation between salary and age — no sign of age-based discrimination.

def print_mean_quantity(df):
    print ("Quantity of people in each department:")          
    quantity = df.groupby(["Department"]).count()["Name"]
    quantity_columns = quantity.to_frame(name="Share (%)").reset_index()
    quantity_columns["Share (%)"] = quantity_columns["Share (%)"] / quantity_columns["Share (%)"].sum()*100
    print(quantity_columns)
    return quantity_columns
departments_quantity=print_mean_quantity(df)
def pie_chart (massiv):
    y = massiv["Share (%)"].values
    labels = massiv["Department"].values
    plt.pie(y, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')  # Makes the pie chart round
    plt.title ("Quantity of people in each department")
    plt.savefig("department_pie_chart.png")  # Save the pie chart
    plt.show()
departments_quantity_chart=pie_chart(departments_quantity)
# According to the data, the Marketing department has the most employees, while HR has the fewest.

# Saving of created dataframe to new txt file
filenew = "/workspaces/dwp_ber_s25_codingfundamentals/homework/Data_project/DataAnalysisResult.txt"
with open(filenew, "a") as f:
    f.write("\n\n--- Mean salary of each department: ---\n")
mean_salary.to_csv(filenew, mode='a')
with open(filenew, "a") as f:
    f.write("\n\n--- Quantity of people in each department ---\n")
departments_quantity.to_csv(filenew, mode='a', index=False)
with open(filenew, "a") as f:
    f.write("\n\n--- Salary Dependence on Age ---\n")
dependence_age_salary.to_csv(filenew, mode='a')
