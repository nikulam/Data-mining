import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.wordnet import WordNetLemmatizer


with open('stopwords.txt') as file:
    stop_words = file.read().splitlines()

symbols = ['', '~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']


df = pd.read_csv('absdata.csv', delimiter='#')

spaces = []
for i in range(0, len(df['id'])):
    spaces.append(' ')

df['spaces'] = spaces
df['combined'] = df['title'] + df['spaces'] + df['abstract']

newCol = []
for i, row in df.iterrows():
    s = row['combined']
    s = s.lower()
    plain = ''.join(n for n in s if n not in symbols)
    words =  plain.split(' ')

    filtered = list(filter(lambda n: n not in stop_words and n != '' and not n.isdigit(), words))

    nouns = list(map(lambda n: WordNetLemmatizer().lemmatize(n), filtered))
    verbs = list(map(lambda n: WordNetLemmatizer().lemmatize(n, 'v'), nouns))

    newCol.append(' '.join(verbs))
    



df.drop('title', axis=1, inplace=True)
df.drop('abstract', axis=1, inplace=True)
df.drop('combined', axis=1, inplace=True)
df.drop('spaces', axis=1, inplace=True)
df['newCol'] = newCol

'''with open('cols.txt', 'w', encoding="utf-8") as file:
    for col in finalColumns:
        file.write(col + "\n")
'''

v = TfidfVectorizer()
resp = v.fit_transform(df['newCol'])
df.drop('newCol', axis=1, inplace=True)
df2 = pd.DataFrame(resp.toarray(), columns=v.get_feature_names())
final = pd.concat([df, df2], axis=1)

for c in final.columns:
    if c.isdigit():
        final.drop(c, axis=1, inplace=True)


final.to_csv('bow.csv', sep='#', index=False)
