import yfinance as yf
import requests
import pandas as pd
from bs4 import BeautifulSoup

import json
import time

# get stock price
df = yf.download('005930.KS','2021-06-03','2023-10-03')
df.to_excel("삼성전자.xlsx")
df.to_csv("삼성전자.csv")

# get news data from naver
news_dic = {}

for index_val in df.index:
    str_index = str(index_val)
    date = str_index[0:4] + str_index[5:7] + str_index[8:10]
    url = 'https://search.naver.com/search.naver?where=news&query='+company+'&sm=tab_opt&sort=0&photo=0&field=0&pd=3&ds='+date+'&de='+date+'&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Afrom'+date+'to'+date+'&is_sug_officeid=0&office_category=0&service_area=0'
    print(url)
    time.sleep(5)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        tag_titles = soup.select('a.news_tit')
        tag_summs = soup.select('a.api_txt_lines.dsc_txt_wrap')
        tmp_list = []
        for title, summ in zip(tag_titles, tag_summs):
            tmp_list.append({'title': title.text, 'summary': summ.text})

        news_dic[str_index] = tmp_list
                # save as json
        with open('samsung_news.json', 'w', encoding='utf-8') as json_file:
            json.dump(news_dic, json_file, ensure_ascii=False, indent=4)

    else:
        print('ERROR')
