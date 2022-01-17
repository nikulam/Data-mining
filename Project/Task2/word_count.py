import pandas as pd
from collections import Counter
from nltk.stem.wordnet import WordNetLemmatizer
import sys
from nltk.grammar import pcfg_demo
sys.stdout.reconfigure(encoding='utf-8')


with open('stopwords.txt') as file:
    stopwords = file.read().splitlines()

symbols = ['', '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']


df1 = pd.read_csv('absdata.csv', delimiter='#')
df2 = pd.read_csv('kmeans2.csv', delimiter='#')

spaces = []
for i in range(0, len(df1['id'])):
    spaces.append(' ')

df1['spaces'] = spaces
df2['combined'] = df1['title'] + df1['spaces'] + df1['abstract']
df2['id'] = df1['id']

df2.drop('i', axis=1, inplace=True)

c0 = []
c1 = []
c2 = []
c3 = []
c4 = []

for i, row in df2.iterrows():
    s = row['combined']
    s = s.lower()
    plain = ''.join(n for n in s if n not in symbols)
    words =  plain.split(' ')

    filtered = list(filter(lambda n: n not in stopwords and n != '' and not n.isdigit(), words))

    nouns = list(map(lambda n: WordNetLemmatizer().lemmatize(n), filtered))
    verbs = list(map(lambda n: WordNetLemmatizer().lemmatize(n, 'v'), nouns))

    if row['cluster'] == 0:
        c0 += verbs
    elif row['cluster'] == 1:
        c1 += verbs
    elif row['cluster'] == 2:
        c2 += verbs
    elif row['cluster'] == 3:
        c3 += verbs
    elif row['cluster'] == 4:
        c4 += verbs


counter0 = Counter(c0)
counter1 = Counter(c1)
counter2 = Counter(c2)
counter3 = Counter(c3)
counter4 = Counter(c4)

print(counter0)
print(counter1)
print(counter2)
print(counter3)
print(counter4)




