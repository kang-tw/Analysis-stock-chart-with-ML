import yfinance as yf
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import pandas  as pd

file_path = "c:\Users\ghdud\Downloads\gpt_result.json"

with open(file_path, 'r') as file:
    data = json.load(file)
    print(type(data))
df_pos_or_neg = pd.DataFrame(list(data.items()),columns=['date','weight'])
df_pos_or_neg.set_index('date', inplace=True)


df = yf.download('005930.KS','2023-01-02','2023-06-30')
df.to_excel("삼성전자.xlsx")
df.to_csv("삼성전자.csv")

from datetime import datetime
converted_keys = [datetime.strptime(key, '%Y-%m-%d %H:%M:%S') for key in data.keys()]
df_w = pd.DataFrame(list(zip(converted_keys, data.values())), columns=['date', 'weight'])
df_w.set_index('date', inplace=True)

result_df = pd.concat([df, df_w], axis=1)
result_df.to_csv('fin_output.csv', encoding='utf-8')