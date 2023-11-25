import tensorflow as tf
from keras import Sequential
from keras.layers import Dense, LSTM, Dropout
from data_processing import train_data,train_result,test_data,test_result ,data_result
from keras.optimizers import Adam
import matplotlib.pyplot as plt
import pandas as pd


path = './fin_output.csv'
csv_data = pd.read_csv(path)





model = Sequential()
model.add(LSTM(units=30, activation='tanh', input_shape=(5, 4),return_sequences=True))
#model.add(Dropout(0.05)) # 과적합 방지 랜덤한 10프로의 모듈 비활성화

model.add(LSTM(units=30, activation='tanh'))
#model.add(Dropout(0.05))   
   

optimizer = Adam(learning_rate=0.001)
model.add(Dense(units=1)) # fully connected layer 최종적인 모델의 결과값을 도출하기 위해 사용 
#model.summary()
model.compile(optimizer=optimizer, loss='mean_squared_error')



with tf.device("/device:GPU:0"): # GPU 설정 명령어 gpu를 인식할 경우 default로 잡을 수 있긴하다. 
    model.fit(train_data, train_result, epochs=100, batch_size=11)
    pred_y = model.predict(test_data)

model.save('model_RNN.h5') # 학습된 데이터중에 잘 학습된 데이터가 존재한다면 모델 키핑


plt.figure()
plt.plot(test_result, color='red', label='real price')
plt.plot(pred_y, color='blue', label='predicted price')
plt.title('price prediction')

plt.xlabel('time')
plt.ylabel('price')


plt.legend()
plt.show()


print("내일 SEC 주가 :", csv_data['Close'].iloc[-1] * pred_y[-1] /data_result[-1], 'KRW')
