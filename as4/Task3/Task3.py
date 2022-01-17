import statistics as stats
import numpy as np
import math
import pandas as pd

u1 = [3,1,2,2,0,2]
u2 = [4,2,3,3,4,2]
u3 = [4,1,3,3,2,5]
u4 = [0,3,4,4,5,0]
u5 = [2,5,5,0,3,3]
u6 = [1,4,0,5,0,0]

u1m = stats.mean(list(filter(lambda n: n != 0, u1)))
u2m = stats.mean(list(filter(lambda n: n != 0, u2)))
u3m = stats.mean(list(filter(lambda n: n != 0, u3)))
u4m = stats.mean(list(filter(lambda n: n != 0, u4)))
u5m = stats.mean(list(filter(lambda n: n != 0, u5)))
u6m = stats.mean(list(filter(lambda n: n != 0, u6)))

#Pearson's correlation coefficient calculated "by hand"
#since only the movies rated by both users are included.

#Helper to remove zeros and corresponding elements from two lists
def dropZeros(arr1, arr2):
    a1 = arr1
    a2 = arr2
    zeros = []

    for i in range(0,6):
        if a1[i] == 0 or a2[i] == 0:
            zeros.append(i)

    for x in zeros[::-1]:
        a1 = a1[:x] + a1[x+1 :]
        a2 = a2[:x] + a2[x+1 :]

    return a1, a2

#Return Pearson's correlation coefficient matrix
def coef(matrix, means, y):
    result = np.zeros((y, y))

    for i in range(0, y):
        for j in range(0, y):
            a, b = dropZeros(matrix[i], matrix[j])
            ma = means[i]
            mb = means[j]
            sumab = 0
            suma2 = 0
            sumb2 = 0
            for n in range(0, len(a)):
                sumab += (a[n] - ma) * (b[n] - mb)
                suma2 += (a[n] - ma) ** 2
                sumb2 += (b[n] - mb) ** 2

            r = sumab / (math.sqrt(suma2) * math.sqrt(sumb2))
            result[i][j] = r

    return result


matrix = [u1, u2, u3, u4, u5, u6]
means = [u1m, u2m, u3m ,u4m, u5m, u6m]

m = coef(matrix, means, 6)
