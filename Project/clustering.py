import sys
from nltk.grammar import pcfg_demo
sys.stdout.reconfigure(encoding='utf-8')
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering
from sklearn.cluster import MeanShift
from sklearn.cluster import AgglomerativeClustering

#Output csv-file from prepro.py
df = pd.read_csv('bow.csv', delimiter='#')
df.drop(['id', 'class'], axis=1, inplace=True)

#Using sklearn's KMeans-method to cluster the data and exporting the results to a csv table.
km = KMeans(n_clusters=5)
km.fit(df.values)
labels = km.labels_
results = pd.DataFrame([df.index,labels]).T

'''spec = SpectralClustering(n_clusters=5)
spec.fit(df.values)
labels = spec.labels_
results = pd.DataFrame([df.index,labels]).T'''

'''agc = AgglomerativeClustering(n_clusters=5, linkage='ward')
agc.fit(df.values)
labels = agc.labels_
results = pd.DataFrame([df.index,labels]).T'''


results.to_csv('kmeans.csv', sep='#', index=False)