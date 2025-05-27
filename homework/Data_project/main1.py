import pandas as pd
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