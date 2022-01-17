import pandas as pd
import statistics as stats
import numpy as np


df = pd.read_csv('ratdataNormChecked.csv')

#print(stats.mean(df['heartind']))
#print(np.percentile(df['gonind'], 20))
#print(sum(i > 5 for i in df['kmethod']))


with open('test.txt', 'w') as wf:
    with open('rattrans2.txt', 'r') as rf:

        for index, row in df.iterrows(): 
            line = rf.readline().split('\n')[0]

            if row['gonind'] <= 0.0452:
                line += ' gonindlow'
            elif row['gonind'] >= 1.504:
                line += ' gonindhigh'
            
            if row['appind'] <= 0.009854:
                line += ' appindlow'
            elif row['appind'] >= 0.017749:
                line += ' appindhigh'

            if row['heartind'] <= 0.003522:
                line += ' heartindlow'
            elif row['heartind'] >= 0.004752:
                line += ' heartindhigh'

            if row['sulcer'] > 1:
                line += ' hassulcer'
            '''
            if row['kmethod'] == 1:
                line += ' kmethodone'
            elif row['kmethod'] == 3:
                line += ' kmethodthree'
            elif row['kmethod'] == 4:
                line += ' kmethodfour'
            '''

            line += '\n'
            
            wf.write(line)
