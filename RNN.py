import tensorflow as tf
from keras import Sequential
from keras.layers import Dense, LSTM, Dropout
from make_namalize import train_data,train_result,test_data,test_result
from keras.optimizers import Adam


model = Sequential()
model.add(LSTM(units=10, activation='relu', input_shape=(5, 4), return_sequences=True))
model.add(Dropout(0.2)) # 과적합 방지 랜덤한 10프로의 모듈 비활성화

model.add(LSTM(units=10, activation='relu'))
model.add(Dropout(0.2))


optimizer = Adam(learning_rate=0.1)
model.add(Dense(units=1)) # fully connected layer 최종적인 모델의 결과값을 도출하기 위해 사용 
#model.summary()
model.compile(optimizer=optimizer, loss='mean_squared_error',metrics='accuracy' )



with tf.device("/device:GPU:0"): # GPU 설정 명령어 gpu를 인식할 경우 default로 잡을 수 있긴하다. 
    model.fit(train_data, train_result, epochs=70, batch_size=1)




#pred_y = model.predict(test_data)

#model.save('model_name.h5') # 학습된 데이터중에 잘 학습된 데이터가 존재한다면 모델 키핑
