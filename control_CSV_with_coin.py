import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# CSV 파일을 불러오기
csv_file_path = './ETHUSDT.csv'

csv_data = pd.read_csv(csv_file_path)






#csv_data.drop('Volume', axis=1, inplace=True)
#csv_data.drop('date', axis=1, inplace=True)





# def make_neg(series):
#     return (series - series.min()) / (series.max() - series.min())

# def create_sequences(data, sequence_length):
#     sequences = []
#     for i in range(len(data) - sequence_length + 1):
#         sequence = data.iloc[i:i + sequence_length].values
#         sequences.append(sequence)
#     return np.array(sequences)



# csv_data['fitting_weight'] = csv_data['weight'] - csv_data['weight'].mean()
# #0~5의 데이터를 -2.5~2.5로 변환

# scaler = StandardScaler()
# csv_data['fitting_weight_scaled'] = scaler.fit_transform(csv_data[['fitting_weight']])
# #fitting_weight 데이터를 0~1의 정규 분포 데이터로 변환
# #csv_data['weighted_avg'] = (csv_data['Open'] + csv_data['High'] + csv_data['Low'] + csv_data['Close']) / 4 * csv_data['fitting_weight_scaled']

# csv_data.drop('weight', axis=1, inplace=True)
# csv_data.drop('Volume', axis=1, inplace=True)
# csv_data.drop('fitting_weight', axis=1, inplace=True)
# csv_data.drop('fitting_weight_scaled', axis=1, inplace=True)






