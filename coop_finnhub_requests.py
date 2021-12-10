import requests
import json
import pandas as pd
import numpy as np

stock = input("please enter a ticker")

finnhub_key = "c5n18haad3iam7tutq70"

payload = {'symbol': stock, 'token': finnhub_key}

base_url = "https://finnhub.io/api/v1/stock/insider-transactions"

r = requests.get(base_url, params = payload)

test = r.content.decode('utf-8')

data = json.loads(test)

data_json = json.dumps(data, indent=4)

print(data_json)


def zip_keys(individual_dict: dict):
    name = individual_dict['name']
    del individual_dict['name']
    return {(name, key): individual_dict[key] for key in individual_dict}

def combine_dict(big_dict):
    combine = {}
    for k in big_dict:
        for key, value in k.items():
            combine[key] = value
    return combine

test = []

for value in data['data']:
    test.append(zip_keys(value))
print(test)

fully_combine_dict = combine_dict(test)
df = pd.DataFrame(fully_combine_dict, index= [0,])
print(df)


