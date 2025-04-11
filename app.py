import pandas as pd
import random
import openpyxl
import numpy as np

data = pd.read_excel('barrettII_eyes_clustering.xlsx')
df = pd.DataFrame(data)
df['Correto'] = df['Correto'].map({'S': 1, 'N': 0})

print(df.info())
print(df.describe())