import pandas as pd

df = pd.read_csv('students.txt', delimiter='\t')

print(df[df['class'] == '5B'])