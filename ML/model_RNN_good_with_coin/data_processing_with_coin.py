import numpy as np
import pandas as pd
from control_CSV_with_coin import csv_data

csv_file_path = './real_result_with_coin.csv'
real_result = pd.read_csv(csv_file_path)
real_result = real_result.iloc[1:, :]

def min_max_Scaler(data):
    return (data - np.min(data, 0) )/ (np.max(data, 0) - np.min(data, 0) + 1e-15)

csv_data = min_max_Scaler(csv_data)
real_result=min_max_Scaler(real_result)

csv_data = csv_data.values.tolist()
real_result = real_result.values.tolist()

data = []
data_result = []

size= 1


for i in range(len(real_result) - size): # 15분의 데이터 4개 마디로 총 1시간의 데이터를 보고 새로운 가격 예측 
    temp_data = csv_data[i : i + size] 
    temp_result = real_result[i + size]     
    data.append(temp_data)
    data_result.append(temp_result)



train_size = int(len(data_result) * 0.8)
train_data = np.array(data[0 : train_size])
train_result = np.array(data_result[1 : train_size+1])



test_data = np.array(data[train_size+1 : ])
test_result = np.array(data_result[train_size+2 : ])


# print(train_data.shape)
# print(train_result.shape)
