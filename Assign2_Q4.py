# Anne Tran (UCID 30286177)
# Assign 2_Q4

import pandas as pd
import numpy as np

df=pd.read_csv("student.csv")# load the dataset into data frame

# Filter the dataset
filteredDF=df[
    (df["studytime"]>3) & # filter student has study time more than 3
    (df["internet"]==1) & # filter student has internet equal 1
    (df["absences"]<=5)] # filter student has absences less or equal to 5

# Load  filtered dataset into new csv file
filteredDF.to_csv("high_engagement.csv", index=False)

# Calc number of student have high engagement
numberOfStudent=len(filteredDF)

# Calc the student's grade
averageGrade=np.mean(filteredDF["grade"])

print(filteredDF)
print(f"Number of student is {numberOfStudent}")
print(f"The average grade is {averageGrade}")