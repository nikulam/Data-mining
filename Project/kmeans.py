import sys
from nltk.grammar import pcfg_demo
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
import numpy as np
import statistics as stats
import math
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.cluster import KMeans

#Using sklearn's KMeans-method to cluster the data and exporting the results to a csv table.

df = pd.read_csv('bow2.csv', delimiter='#')
df.drop(['id', 'class'], axis=1, inplace=True)

km = KMeans(n_clusters=5)
km.fit(df.values)
labels = km.labels_
results = pd.DataFrame([df.index,labels]).T

results.to_csv('kmeans2.csv', sep='#', index=False)
