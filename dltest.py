import requests
import json
import urllib
import csv

import pandas as pd
df = pd.read_csv('https://api.llama.fi/simpleChainDataset/Ethereum?staking=true&doublecounted=true&liquidstaking=true')

#print(df)
#print(df.iloc[0,-1])

json_row = df.iloc[0:1].to_json(orient='records')
print(json_row)

# ethtvl = df.iloc[0]
# ethtvl_latest = df.iloc[0,-1]

# print(total)