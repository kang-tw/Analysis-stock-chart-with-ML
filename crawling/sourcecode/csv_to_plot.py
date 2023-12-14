import numpy as np
import pandas as pd

tsv_ground_truth = '../pred_csvs/samsung_output.csv'
tsv_pred = '../pred_csvs/samsung_pred_output.csv'
tsv_date = '../pred_csvs/samsung_origin.tsv'


# 예측데이터와 원본 데이터 가져오기
np_truth = np.genfromtxt(tsv_ground_truth)
np_pred = np.genfromtxt(tsv_pred)

# 타임스태프를 위한 파일 불러오기
df = pd.read_csv(tsv_date, sep=',')
df_time = df.iloc[:, 0].values

samsung_data = {'date': df_time,'real price': np_truth,'predicted price': np_pred}
df_samsung = pd.DataFrame(samsung_data)
tsv_file_path = 'plot_samsung.tsv'
df_samsung.to_csv(tsv_file_path, sep='\t', index=False)

tsv_ground_truth = '../pred_csvs/ETH_output.csv'
tsv_pred = '../pred_csvs/ETH_pred_output.csv'
tsv_date = '../pred_csvs/eth_origin.csv'


# 예측데이터와 원본 데이터 가져오기
np_truth = np.genfromtxt(tsv_ground_truth)
np_pred = np.genfromtxt(tsv_pred)

# 타임스태프를 작성
def generate_timestamps(start_date, end_date, n):
    total_days = (end_date - start_date).days
    interval = timedelta(days=total_days / (n - 1))

    timestamps = [start_date + i * interval for i in range(n)]

    return timestamps

# 시작 날짜와 종료 날짜 설정
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 11, 25)

# n개의 타임스탬프 생성
n = 6316
timestamps = generate_timestamps(start_date, end_date, n)

# 넘파이 어레이로 변환
timestamps_np = np.array(timestamps, dtype='datetime64')

# 년, 월, 일만 남기기
df_time = np.datetime_as_string(timestamps_np, unit='D')

eth_data = {'date': df_time,'real price': np_truth,'predicted price': np_pred}
df_eth = pd.DataFrame(eth_data)
tsv_file_path = 'plot_eth.tsv'  # 저장할 파일 경로 및 이름
df_eth.to_csv(tsv_file_path, sep='\t', index=False)

