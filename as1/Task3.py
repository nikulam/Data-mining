import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
from sklearn.decomposition import PCA
from sklearn import preprocessing

data = np.matrix([[0,1], [-1/2,3/2], [3/2,5/2], [1,3]])
data2 = np.matrix([[1,2,3,4], [5,5,6,7], [1,4,2,3], [5,3,2,1], [8,1,2,2]])
df = pd.DataFrame(data, columns=['f1', 'f2'])
df2 = pd.DataFrame(data2, columns=['f1','f2','f3','f4'])
#scale the data so that mean = 0, std = 1
data3 = np.zeros((4,2))
ka = df.mean()
kh = df.std()

for y in range(0,2):
    for x in range(0,4):
        data3[x,y] = ((data[x,y] - ka[y]) / kh[y])

df3 = pd.DataFrame(data3, columns=['f1','f2'])
print(df3)

#covariance matrix
c = np.cov(df3.T, bias=False)
print(c)

v = np.linalg.eig(c)
print(v)


##print(np.matmul(c, ))
##print(np.linalg.eigvals(c))


##plt.scatter([0,-1/2, 3/2, 1], [1,3/2, 5/2, 3])
##plt.show()

e1 = [1,1]
e2 = [-1,1]
eigenvectors = [e1, e2]

##print(np.matmul(scaled, eigenvectors))

df_std = (df - df.mean()) / (df.std())
pca = PCA(n_components=2)
components = pca.fit_transform(df_std)
principalDf = pd.DataFrame(data=components,columns=['nf'+str(i+1) for i in range(2)])


'''pca = PCA()
pca.fit(scaled)
pca_data = pca.transform(scaled)
per = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
plt.bar(x=range(1, len(per) + 1), height=per)
plt.show()
'''