import numpy as np
import pandas as pd
from keras import Input
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from paths.path import dir_path
from keras.layers import Dense, LSTM, concatenate
from keras.models import Sequential, Model, load_model
from abc import abstractmethod, ABCMeta

#날짜                종가      오픈      고가      저가      거래량    변동 %

class Samsung_Stock_Service(metaclass=ABCMeta):


    def __init__(self):
        global path, DNN, LSTM
        path = dir_path('aitrader')
        DNN = load_model(f'{path}\\save\\DNN.h5')
        LSTM = load_model(f'{path}\\save\\LSTM.h5')

    def hook(self):
        return 'a'
    def DNN_scaled(self,x):

        x = np.array(x)
        x = np.reshape(x, (1,x.shape[0] * x.shape[1])).astype(float)

        print(f'#######################{x}')

        scalar = StandardScaler()
        scalar.fit(x)
        x_scaled = scalar.transform(x)
        print(type(x_scaled))
        return x_scaled
    def normalization(self, df):
        df2 = df
        for i in range(len(df2.index)):
            for j in range(len(df2.iloc[i])):
                if j ==0:
                    df2.iloc[i, j] = df2.iloc[i, j].replace(' ', '')
                else:
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

    def preprocessing(self):
        path = dir_path('aitrader')
        df1 = pd.read_csv(f'{path}\\data\\test.csv',header=0, encoding='utf-8', sep=',')
        del df1['변동 %']
        df1 = df1.astype('str')
        df1.replace(np.nan, '0', regex=True, inplace=True)
        df1['날짜'] = df1['날짜'].replace(" ", '')
        df1 = df1[df1['거래량'] != '0']
        self.normalization(df1)
        df1.sort_values(['날짜'], ascending=[True], inplace=True)

        return df1

    def extract_5_days(self):
        df = self.preprocessing()
        #df['날짜'] = pd.to_datetime(df['날짜'])
        df = df.loc[:, '2022-12-01':'2022-12-03']
        print(df)



        #df['날짜'] = pd.to_datetime(df['날짜'])
        #df = df[df['날짜'].between(date+pd.Timedelta(days=5),date)]


    def DNN_predict(self):
        x = [[70200.0, 71600.0, 71600.0, 70200.0, 12610000.0],
             [70600.0, 70300.0, 70600.0, 69800.0, 590.0],
             [70500.0, 70400.0, 70900.0, 70100.0, 4890.0],
             [70200.0, 70300.0, 70900.0, 70200.0, 980.0],
             [69900.0, 69900.0, 70000.0, 69600.0, 11440000.0]]
        x_scaled =self.DNN_scaled(x)
        y_pred = DNN.predict(x_scaled)
        print(y_pred[0])



# 5일 동안의   종가      오픈      고가      저가      거래량을 토대로 6일 째 종가를 예측하는 모델

if __name__ == '__main__':

    s = Samsung_Stock_Service()
    s.extract_5_days()
