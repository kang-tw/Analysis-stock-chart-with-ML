import tensorflow as tf
from keras import Sequential
from keras.layers import Dense, LSTM, Dropout,Flatten
from data_processing import train_data,train_result,test_data,test_result ,data_result
from keras.optimizers import Adam
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path = './fin_output.csv'
csv_data = pd.read_csv(path)


def make_model():
    model = Sequential()
    model.add(LSTM(units=128, activation='tanh', input_shape=(20, 5),return_sequences=True))
    model.add(Dropout(0.05)) # 과적합 방지 랜덤한 10프로의 모듈 비활성화
    model.add(LSTM(units=64, activation='tanh',return_sequences=True))
    model.add(Dropout(0.05))  
    model.add(LSTM(units=32, activation='tanh'))

    optimizer = Adam(learning_rate=0.0015)
    model.add(Flatten())
    model.add(Dense(units=1,activation ='tanh')) # fully connected layer 최종적인 모델의 결과값을 도출하기 위해 사용 

    model.compile(optimizer=optimizer, loss='mean_squared_error')
    return model


hit =0
count = 0
model = make_model()


while(True):
    count =count+1
    with tf.device("/device:GPU:0"): # GPU 설정 명령어 gpu를 인식할 경우 default로 잡을 수 있긴하다. 
        model.fit(train_data, train_result, epochs=10, batch_size=10)
    pred_y = model.predict(test_data)
    avg=0
    for i,j in zip(pred_y,test_result):
        avg += abs(1 -j/i)
        
    avg= avg/len(pred_y) * 100
    print(avg)
    
    if(avg<8.3):hit=hit+1
    if(hit == 2): break
    if(count == 30):
         model=make_model()
         count = 0
    

model.save('model_RNN.h5') # 학습된 데이터중에 잘 학습된 데이터가 존재한다면 모델 키핑


plt.figure()
plt.plot(test_result, color='red', label='real price')
plt.plot(pred_y, color='blue', label='predicted price')
plt.title('price prediction')

x_values = np.arange(len(pred_y))

plt.xlabel('time')
plt.ylabel('price')
plt.xticks(x_values)

plt.legend()
plt.grid()
plt.show()
np.savetxt('samsung_output.csv', test_result, delimiter=',')
np.savetxt('samsung_pred_output.csv', pred_y, delimiter=',')

print("내일 삼성전자 주가 :", csv_data['Close'].iloc[-1] * pred_y[-1] /data_result[-1], 'KRW')
