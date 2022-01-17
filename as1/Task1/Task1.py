import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import statistics


df = pd.read_csv('corrtestdata.csv')

#remove outliers
i = 0
indices = []
for row in df['id']:
    if row in ['rat2', 'rat53', 'rat120', 'rat434']:
        indices.append(i)
    i+=1



df.drop(indices, inplace=True)

#remove freezed
i = 0
indices = []
for row in df['day']:
    if row == 400:
        indices.append(i)
    i+=1

df.drop(indices, inplace=True)


df.loc[df['kmethod'] == 1, 'kmethod'] = 10

#remove ratID
df.drop(columns=['id'], inplace=True)

##change freezed
##df.loc[df['day'] == 400, 'day'] = 0
##df.loc[df['year'] == 15, 'year'] = -1

c = df.corr().abs().round(3)

sorted = s = c.unstack().sort_values()


plt.figure(figsize = (15, 15))
sns.heatmap(c, annot = True)

##plt.matshow(df.corr())
plt.show()
