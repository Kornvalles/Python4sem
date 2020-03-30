import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('FOLK1A.csv', encoding='utf-8', delimiter=';')
#print(df)
#print(df.at[100, 'INDHOLD'])
#legal_age = df[1:]['ALDER'] < 18
#print(legal_age)
non_married = df.loc[df['CIVILSTAND'] == 'Ugift']['INDHOLD']
married = df.loc[df['CIVILSTAND'] == 'Gift/separeret']['INDHOLD']
widdow = df.loc[df['CIVILSTAND'] == 'Enke/enkemand']['INDHOLD']
divorced = df.loc[df['CIVILSTAND'] == 'Fraskilt']['INDHOLD']
ax = pd.concat([non_married, married, widdow, divorced], axis=1, keys=['Ugift', 'Gift/separeret', 'Enke/enkemand', 'Fraskilt'])
ax.plot()
ax.show()
#print(type(non_married))
#print(ax)
#print(non_married)
