import tensorflow as tf
from keras import Sequential
from keras.layers import Dense, LSTM, Dropout
from data_processing_with_coin import train_data,train_result
from keras.optimizers import Adam






model = Sequential()
model.add(LSTM(units=100, activation='tanh', input_shape=(1, 5),return_sequences=True))
model.add(Dropout(0.1)) # 과적합 방지 랜덤한 10프로의 모듈 비활성화

model.add(LSTM(units=100, activation='tanh'))
model.add(Dropout(0.1))   
    

optimizer = Adam(learning_rate=0.003)
model.add(Dense(units=1)) # fully connected layer 최종적인 모델의 결과값을 도출하기 위해 사용 
#model.summary()
model.compile(optimizer=optimizer, loss='mean_squared_error')



with tf.device("/device:GPU:0"): # GPU 설정 명령어 gpu를 인식할 경우 default로 잡을 수 있긴하다. 
    model.fit(train_data, train_result, epochs=50, batch_size=200)
 

model.save('model_RNN.h5') # 학습된 데이터중에 잘 학습된 데이터가 존재한다면 모델 키핑

