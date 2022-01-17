import pandas as pd
import math
import matplotlib.pyplot as plt

df1 = pd.read_csv('absdata.csv', delimiter='#')

#Output csv-file from clustering.py
df2 = pd.read_csv('kmeans2.csv', delimiter='#')

df = pd.DataFrame({'id': df1['id'], 'class': df1['class'], 'cluster': df2['1']})

Mi = 0.0
Hc = 0.0
Hd = 0.0
n = len(df['class'])

for c in range(0,5):
    Pc = len(df[df['cluster'] == c]) / n
    Hc += Pc * math.log(Pc)

    for d in range(1,6):
        Pd = len(df[df['class'] == d]) / n

        l = len(df[(df['class'] == d) & (df['cluster'] == c)])
        if l > 0:
            Pcd = l / n
            Mi += Pcd * math.log((Pcd / (Pc * Pd)))
        else:
            Pcd = 0

for d in range(1, 6):
    Pd = len(df[df['class'] == d]) / n
    Hd += Pd * math.log(Pd)


print(Mi / math.sqrt(Hc * Hd))