from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

df = pd.read_csv('bow.csv', delimiter='#')
df.drop(['id', 'class'], axis=1, inplace=True)

pca = PCA(n_components=75)
pca_result = pca.fit_transform(df)

print('Cumulative variance: {:.2%}'.format(np.sum(pca.explained_variance_ratio_)))

df2 = pd.DataFrame(pca_result)

df2.to_csv('pca.csv', sep='#', index=False)