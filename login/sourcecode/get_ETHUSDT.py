import requests
from datetime import datetime
import time
import pandas as pd
from tqdm import tqdm
result = requests.get('https://api.binance.com/api/v3/ticker/price')
COLUMNS = ['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'quote_av', 'trades', 
                   'tb_base_av', 'tb_quote_av', 'ignore']
URL = 'https://api.binance.com/api/v3/klines'
def get_data(start_date, end_date, symbol):
    data = []
    
    start = int(time.mktime(datetime.strptime(start_date + ' 00:00', '%Y-%m-%d %H:%M').timetuple())) * 1000
    end = int(time.mktime(datetime.strptime(end_date +' 23:59', '%Y-%m-%d %H:%M').timetuple())) * 1000
    # set interval time is 15m
    params = {
        'symbol': symbol,
        'interval': '15m',
        'limit': 1000,
        'startTime': start,
        'endTime': end
    }
    # get crawl data from binace
    while start < end:
        params['startTime'] = start
        result = requests.get(URL, params = params)
        js = result.json()
        if not js:
            break
        data.extend(js)
        start = js[-1][0] + 60000
    # preprocessing
    df = pd.DataFrame(data)
    df.columns = COLUMNS
    df['Open_time'] = df.apply(lambda x:datetime.fromtimestamp(x['Open_time'] // 1000), axis=1)
    df = df.drop(columns = ['Close_time', 'ignore','quote_av','trades','tb_base_av','tb_quote_av'])
    df['Symbol'] = symbol

    return df

start_date = '2023-01-01'
end_date = '2023-11-25'
df_result = get_data(start_date, end_date, 'ETHUSDT')
df_result.set_index('Open_time', inplace=True)
df_result.to_csv('ETHUSDT.csv', encoding='utf-8')