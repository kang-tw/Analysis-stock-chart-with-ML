import tensorflow as tf
from keras import Model
from keras.layers import Dense, LSTM, Dropout, Conv2D,pooling, Reshape
from data_processing import train_data,train_result,test_data,test_result
from keras.optimizers import Adam
import keras.layers as layers
import matplotlib.pyplot as plt



# conv1 = keras.layers.Conv2D(filters = 6, kernel_size = (3, 3), padding = 'same', name = 'conv1_6_filters')(inp)
# conv1 = keras.layers.pooling.MaxPooling2D(pool_size = (2, 2), padding = 'valid', name = 'maxpooling1', strides = None)(conv1)



input_layer = layers.Input(shape = (20,4,1))

convolution_lay = Conv2D(filters = 1, kernel_size = (2, 2), padding = 'same', name = 'conv1_6_filters')(input_layer)
convolution_lay = pooling.MaxPooling2D(pool_size = (2, 1), padding = 'same', name = 'maxpooling1', strides = None)(convolution_lay)

flatten = layers.Flatten(name = 'flatten')(convolution_lay)
reshape = layers.Reshape((10, 4))(flatten) 

RNN1_lay = LSTM(units=10, activation='sigmoid', return_sequences=True)(reshape)
RNN1_layDropout = Dropout(0.2)(RNN1_lay) # 과적합 방지 랜덤한 10프로의 모듈 비활성화

RNN2_lay = LSTM(units=10, activation='sigmoid')(RNN1_lay)
RNN2_lay = Dropout(0.2)(RNN2_lay)

output_layer = Dense(units=1)(RNN2_lay) # fully connected layer 최종적인 모델의 결과값을 도출하기 위해 사용 

#model.summary()
optimizer = Adam(learning_rate=0.1)
model = Model(input_layer, output_layer)

model.compile(optimizer=optimizer, loss='mean_squared_error')


with tf.device("/device:GPU:0"): # GPU 설정 명령어 gpu를 인식할 경우 default로 잡을 수 있긴하다. 
    model.fit(train_data, train_result, epochs=100, batch_size=20)

pred_y = model.predict(test_data)

#model.save('model_name.h5') # 학습된 데이터중에 잘 학습된 데이터가 존재한다면 모델 키핑

plt.figure()
plt.plot(test_result, color='red', label='real price')
plt.plot(pred_y, color='blue', label='predicted SEC price')
plt.title('SEC stock price prediction')

plt.xlabel('time')
plt.ylabel('stock price')


plt.legend()
plt.show()