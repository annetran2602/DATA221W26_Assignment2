# Anne Tran (UCID: 30286177)
# Assign2_Q6

import pandas as pd
df=pd.read_csv("crime.csv") # load dataset into dataframe

def classifyRisk(crime): # classify the level of risk
    if crime>=0.50:
        return "HighCrime"
    else:
        return "LowCrime"

df["risk"]=df["ViolentCrimesPerPop"].apply(classifyRisk) # classify based on violent crime ratio

# Create the summary table
summaryTable=df.groupby("risk").agg(
    PctUnemployed=("PctUnemployed", "mean") # calc average unemployment rate for each level of risk
)

print(summaryTable) # display the result

