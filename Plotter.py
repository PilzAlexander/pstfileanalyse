import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


headers = ['SpamWords', 'Hits']

df = pd.read_csv('SpamWordHits.csv')

print(df)

df.plot(kind='barh', x='Hits', y='SpamWords')




#df = df[df['Hits'] > 1000]

