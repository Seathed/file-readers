import pandas as pd

def printDataFrame(fileName):
    df = pd.read_excel(fileName)
    print(df)