#calculating maximum common subgraph distances with
#1. Udist
#2. Mdist

def Udist(G1, G2, MCS):
    dist = 1 - MCS / (G1 + G2 - MCS)
    return dist

def Mdist(G1, G2, MCS):
    dist = 1 - MCS / max(G1, G2)
    return dist

G1 = 13
G2 = 11
G3 = 11
G4 = 15
G5 = 14
G6 = 17

MCS = 5

print('Udist: ' + str(Udist(G6, G5, MCS)))
print('Mdist: ' + str(Mdist(G6, G5, MCS)))