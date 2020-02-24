import pandas as pd

url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=Code&delimiter=Semicolon&OMR%C3%85DE=101&CIVILSTAND=G&Tid=*&ALDER=*'
dst = pd.read_json(url)
dst.to_csv('FOLK1A.csv', encoding='utf-8', index=False)
print(dst[:20])