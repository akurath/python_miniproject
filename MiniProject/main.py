# This is a Python script regarding to read csv file.
import pandas as pd
import os.path

inputfile_name = "D:\\Projects\\Freelancer\\Python\\MiniProject\\input\\projectmini.csv"
output_file_name = "D:\\Projects\\Freelancer\\Python\\MiniProject\\output\\projectmini.csv"

if os.path.exists(output_file_name) == True:
        f = open(output_file_name, "w+")
        f.close()
#import csv file

dataFrame = pd.read_csv(inputfile_name)
print("Our dataframe....\n",dataFrame)
# print(dataFrame.head())
# create a dataframe object
df = pd.DataFrame(dataFrame)

# show the dataframe
# print(df)

arr1 = []
arr2 = []
arr3 = []
first = []
second = []
third = []
for i in list(df):
    arr1.append(df[i].iloc[0])
    arr2.append(df[i].iloc[1])
    arr3.append(df[i].iloc[2])

first.append(arr1[0] +" " + arr1[1])
second.append(arr2[0] +" " + arr2[1])
third.append(arr3[0] +" " + arr3[1])

writingFile = pd.DataFrame([[arr1[0], arr1[1],arr1[2],arr1[0] +" " + arr1[1]],[arr2[0], arr2[1],arr2[2],arr2[0] +" " + arr2[1]],[arr3[0], arr3[1], arr3[2],arr3[0] +" " + arr3[1]] ], columns=['first_name', 'last_name','age','full_name'])
writingFile.to_csv(output_file_name, index=False)
print("file write successfully")