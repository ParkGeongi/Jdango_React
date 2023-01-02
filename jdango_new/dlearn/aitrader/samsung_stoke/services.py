import numpy as np
import pandas as pd
from keras import Input
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from paths.path import dir_path
from keras.layers import Dense, LSTM, concatenate
from keras.models import Sequential, Model


class Samsung_stok(object):
    def __init__(self):
        pass
#날짜                종가      오픈      고가      저가      거래량    변동 %
    def normalization(self,df):
        df2 = df
        for i in range(len(df2.index)):
            for j in range(len(df2.iloc[i])):
                if df2.iloc[i, j][-1] == "M":
                    df2.iloc[i, j] = df2.iloc[i, j].replace(',', '')
                    df2.iloc[i, j] = df2.iloc[i, j].replace('M', '')
                    df2.iloc[i, j] = float(df2.iloc[i, j])
                    df2.iloc[i, j] = df2.iloc[i, j] * 1000000

                elif df2.iloc[i, j][-1] == "K":
                    df2.iloc[i, j] = df2.iloc[i, j].replace(',', '')
                    df2.iloc[i, j] = df2.iloc[i, j].replace('K', '')
                    df2.iloc[i, j] = float(df2.iloc[i, j])
                    df2.iloc[i, j] = df2.iloc[i, j] * 1000
                else:
                    df2.iloc[i,j] = df2.iloc[i, j].replace(',', '')
                    df2.iloc[i, j] = float(df2.iloc[i, j])

    def preprocess1(self):
        path = dir_path('aitrader')
        df1 = pd.read_csv(f'{path}\\data\\코스피200내역1.csv',index_col=0, header=0, encoding='utf-8', sep=',')
        df2 = pd.read_csv(f'{path}\\data\\삼성전자.csv', index_col=0, header=0, encoding='utf-8', sep=',')
        del df1['변동 %']
        del df2['변동 %']
        df1 = df1.astype('str')
        df1.replace(np.nan, '0', regex=True, inplace=True)
        df2.replace(np.nan, '0', regex=True, inplace=True)
        df1 = df1[df1['거래량'] != '0']
        df2 = df2[df2['거래량'] != '0']

        self.normalization(df1)
        self.normalization(df2)


        df1.sort_values(['날짜'], ascending=[True], inplace=True)
        df2.sort_values(['날짜'], ascending=[True], inplace=True)

        df1 = df1.values
        df2 = df2.values
        print(type(df1), type(df2))
        print(df1.shape,df2.shape)
        np.save(f'{path}\\save\\kospi.npy', arr = df1)
        np.save(f'{path}\\save\\samsung.npy', arr = df2)

    def split_xy5(self,dataset, time_step, y_column):
        x,y = list(), list()
        for i in range(len(dataset)):
            x_end_number = i + time_step
            y_end_number = x_end_number + y_column
            if y_end_number > len(dataset): break

            tmp_x = dataset[i:x_end_number,:]
            tmp_y = dataset[x_end_number:y_end_number, 0] # 종가
            x.append(tmp_x)
            y.append(tmp_y)
        return np.array(x), np.array(y)

    def DNN(self):
        path = dir_path('aitrader')
        kospi = np.load(f'{path}\\save\\kospi.npy',allow_pickle=True)
        samsung = np.load(f'{path}\\save\\samsung.npy',allow_pickle=True)
        print(kospi)
        print(samsung)
        x,y = self.split_xy5(samsung,5,1)
        print(x.shape)#(468, 5, 5)
        print(y.shape)#(468, 1)

        x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1,test_size=0.3)
        print(x_train.shape) #(327, 5, 5)
        print(x_test.shape) #(141, 5, 5)
        print(y_train.shape) #(327, 1)
        print(y_test.shape) #(141, 1)

        x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1] * x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test, (x_test.shape[0],x_test.shape[1] * x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test= y_test.astype(float)
        scalar = StandardScaler()
        scalar.fit(x_train)
        x_train_scaled = scalar.transform(x_train)
        x_test_scaled = scalar.transform(x_test)
        print(x_train_scaled[0,:])
        print(x_test_scaled.shape)
        model = Sequential()
        model.add(Dense(64,input_shape=(25,)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss= 'mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience = 20)

        model.fit(x_train_scaled, y_train, validation_split=0.2,verbose=1,batch_size=1,epochs=100,callbacks=[early_stopping])
        loss, mse = model.evaluate(x_test_scaled,y_test,batch_size=1)
        model.save(r'C:\Users\AIA\project\jdango_new\dlearn\aitrader\save\DNN.h5')
        print('loss : ', loss)
        print('mse: ', mse)

        y_pred = model.predict(x_test_scaled)

        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')

    def LSTM(self):
        path = dir_path('aitrader')
        kospi = np.load(f'{path}\\save\\kospi.npy', allow_pickle=True)
        samsung = np.load(f'{path}\\save\\samsung.npy', allow_pickle=True)
        print(kospi)
        print(samsung)
        x, y = self.split_xy5(samsung, 5, 1)
        print(x.shape)  # (468, 5, 5)
        print(y.shape)  # (468, 1)

        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        print(x_train.shape)  # (327, 5, 5)
        print(x_test.shape)  # (141, 5, 5)
        print(y_train.shape)  # (327, 1)
        print(y_test.shape)  # (141, 1)

        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test = y_test.astype(float)
        scalar = StandardScaler()
        scalar.fit(x_train)
        x_train_scaled = scalar.transform(x_train)
        x_test_scaled = scalar.transform(x_test)
        print(x_train_scaled[0, :])
        print(x_test_scaled.shape)
        x_train_scaled = np.reshape(x_train_scaled, (x_train_scaled.shape[0],5,5))
        x_test_scaled = np.reshape(x_test_scaled, (x_test_scaled.shape[0],5,5))
        print(x_train_scaled.shape)
        print(x_test_scaled.shape)
        model = Sequential()
        model.add(LSTM(64,input_shape=(5,5)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1))
        model.compile(loss= 'mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience = 20)

        model.fit(x_train_scaled, y_train, validation_split=0.2,verbose=1,batch_size=1,epochs=100,callbacks=[early_stopping])
        loss, mse = model.evaluate(x_test_scaled,y_test,batch_size=1)
        model.save(r'C:\Users\AIA\project\jdango_new\dlearn\aitrader\save\LSTM.h5')
        print('loss : ', loss)
        print('mse: ', mse)

        y_pred = model.predict(x_test_scaled)

        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')

    def DNN_Ensemble(self):
        path = dir_path('aitrader')
        kospi = np.load(f'{path}\\save\\kospi.npy', allow_pickle=True)
        samsung = np.load(f'{path}\\save\\samsung.npy', allow_pickle=True)
        print(kospi)
        print(samsung)
        x, y = self.split_xy5(samsung, 5, 1)
        x2, y2 = self.split_xy5(kospi, 5, 1)

        print(x.shape)  # (468, 5, 5)
        print(y.shape)  # (468, 1)
        print(x2.shape)
        print(y2.shape)


        x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.3)
        print(x_train.shape)  # (327, 5, 5)
        print(x_test.shape)  # (141, 5, 5)
        print(y_train.shape)  # (327, 1)
        print(y_test.shape)  # (141, 1)
        x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, random_state=1, test_size=0.3)
        print(x2_train.shape)
        print(x2_test.shape)
        print(y2_train.shape)
        print(y2_test.shape)

        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1] * x_train.shape[2])).astype(float)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1] * x_test.shape[2])).astype(float)
        y_train = y_train.astype(float)
        y_test = y_test.astype(float)
        scalar = StandardScaler()
        scalar.fit(x_train)
        x_train_scaled = scalar.transform(x_train)
        x_test_scaled = scalar.transform(x_test)
        print(x_train_scaled.shape)
        print(x_test_scaled.shape)

        x2_train = np.reshape(x2_train, (x2_train.shape[0], x2_train.shape[1] * x2_train.shape[2])).astype(float)
        x2_test = np.reshape(x2_test, (x2_test.shape[0], x2_test.shape[1] * x2_test.shape[2])).astype(float)
        y2_train = y2_train.astype(float)
        y2_test = y2_test.astype(float)
        scalar = StandardScaler()
        scalar.fit(x_train)
        x2_train_scaled = scalar.transform(x2_train)
        x2_test_scaled = scalar.transform(x2_test)
        print(x2_train_scaled.shape)
        print(x2_test_scaled.shape)


        input1 = Input(shape=(25,))
        dense1 = Dense(64)(input1)
        dense1 = Dense(32)(dense1)
        dense1 = Dense(32)(dense1)
        output1 = Dense(32)(dense1)

        input2 = Input(shape=(25,))
        dense2 = Dense(64)(input2)
        dense2 = Dense(32)(dense2)
        dense2 = Dense(32)(dense2)
        output2 = Dense(32)(dense2)

        merge = concatenate([output1,output2])
        output3 = Dense(1)(merge)
        model = Model(inputs = [input1,input2], outputs = [output3])


        model.compile(loss='mse', optimizer='adam', metrics=['mse'])

        early_stopping = EarlyStopping(patience=20)

        model.fit([x_train_scaled, x2_train_scaled], y_train, validation_split=0.2, verbose=1, batch_size=1, epochs=100,
                  callbacks=[early_stopping])
        loss, mse = model.evaluate([x_test_scaled,x2_test_scaled], y_test, batch_size=1)
        model.save(r'C:\Users\AIA\project\jdango_new\dlearn\aitrader\save\DNN_Ensemble.h5')
        print('loss : ', loss)
        print('mse: ', mse)

        y_pred = model.predict([x_test_scaled,x2_test_scaled])

        for i in range(5):
            print(f'종가 : {y_test[i]}, 예측가 : {y_pred[i]}')

    def LSTM_Ensemble(self):
        pass

if __name__ == '__main__':

    s = Samsung_stok()
    s.DNN_Ensemble()
