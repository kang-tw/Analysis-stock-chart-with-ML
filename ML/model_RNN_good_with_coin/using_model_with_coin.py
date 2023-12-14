import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data_processing_with_coin import test_result ,data_result,test_data
# 모델 불러오기

model_path = './model_RNN.h5'
model = tf.keras.models.load_model(model_path)

  
file_path = './real_result_with_coin.csv'
csv_data = pd.read_csv(file_path)

# 모델 요약 정보 출력
model.summary()

pred_y = model.predict(test_data)


plt.figure()
plt.plot(test_result, color='red', label='real price')
plt.plot(pred_y, color='blue', label='predicted price')
plt.title('price prediction')

x_values = np.arange(len(pred_y))

plt.xlabel('time')
plt.ylabel('price')
#plt.xticks(x_values)

plt.legend()
plt.grid()
plt.show()





print("이번 이더리움 가격:", csv_data['Close'].iloc[-1] * pred_y[-1] /data_result[-1], 'USD')



# def min_max_Scaler(data):
#     return (data - np.min(data, 0) )/ (np.max(data, 0) - np.min(data, 0) + 1e-15)
