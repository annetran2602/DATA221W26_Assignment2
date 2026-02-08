# Anne Tran (UCID: 30286177)
# Assign 2_Q5

import pandas as pd
import numpy as np

df=pd.read_csv("student.csv") # load dataset into dataframe

def classifyGrade(grade):
    if grade<=9:
        return "Low"
    elif grade >=15:
        return "High"
    else:
        return "Medium"

df["grade_band"]=df["grade"].apply(classifyGrade) # use .apply() to classify the grade in to 3 categories (high, low and medium)

# Create summary table
summaryTable=df.groupby("grade_band").agg(
    numberOfStudent=("grade", "count"),
    averageAbsense=("absences", "mean"),
    percentInternet=("internet", "mean"))
summaryTable["percentInternet"]*=100

summaryTable.to_csv("student_bands.csv", index=False)

