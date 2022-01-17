from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd
import sys
from nltk.grammar import pcfg_demo
sys.stdout.reconfigure(encoding='utf-8')
from collections import Counter
import nltk
from nltk.corpus import stopwords

stop_words = (stopwords.words('english'))
stop_words += ['f', 'w']
print(stop_words)

#df = pd.read_csv('bow.csv', delimiter='#')



l = [1, 2, 3, 4, 5]
l2 = [6,7,8,9,10]

l += l2
print(l)


'''l = ['abnormal', 'abnormally', 'abnormality']

m = list(map(lambda n: WordNetLemmatizer().lemmatize(n, 'v'), l))
print(m)'''