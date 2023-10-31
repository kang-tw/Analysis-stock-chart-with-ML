from keras import Sequential
from keras.layers import Dense, LSTM, Dropout


model = Sequential()

model.add(LSTM(units=20, activation='relu', input_shape=(10, 4)))
model.add(Dropout(0.1)) # 과적합 방지 랜덤한 10프로의 모듈 비활성화

model.add(LSTM(units=20, activation='relu'))
model.add(Dropout(0.1))


model.add(Dense(units=1)) # fully connected layer 최종적인 모델의 결과값을 도출하기 위해 사용 
model.summary()





model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(전처리 데이터 값, 전처리 결과값, epochs=70, batch_size=30)
model.save('model_name.h5') # 학습된 데이터중에 잘 학습된 데이터가 존재한다면 모델 키핑

pred_y = model.predict(test_X) # 예측된 y값 