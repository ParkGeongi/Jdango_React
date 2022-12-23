import pandas as pd

from keras import Sequential
from keras.layers import Dense
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras

class MMFCModel(object):
    def __init__(self):
        pass

    def preprocess(self):
        df = pd.read_csv(r'C:\Users\AIA\project\jdango_new\ml\squart\data\증가증가5개라벨.csv')
        df = (df - df.mean()) / df.std()
        print(df.sample(5))
    def split(self):
        df = pd.read_csv(r'C:\Users\AIA\project\jdango_new\ml\squart\data\증가증가5개라벨.csv')
        train, test = train_test_split(df, test_size=0.2)
        #train, val = train_test_split(train, test_size=0.15)
        X_train = train[
            ['x[0]', 'x[1]', 'x[2]', 'x[3]', 'x[4]', 'x[5]', 'x[6]', 'x[7]', 'x[8]', 'x[9]', 'x[10]', 'x[11]', 'x[12]',
             'x[13]', 'x[14]', 'x[15]', 'x[16]', 'x[17]', 'x[18]', 'x[19]', 'x[20]', 'x[21]', 'x[22]', 'x[23]', 'x[24]',
             'y[0]', 'y[1]', 'y[2]', 'y[3]', 'y[4]', 'y[5]', 'y[6]', 'y[7]', 'y[8]', 'y[9]', 'y[10]', 'y[11]', 'y[12]',
             'y[13]', 'y[14]', 'y[15]', 'y[16]', 'y[17]', 'y[18]', 'y[19]', 'y[20]', 'y[21]', 'y[22]', 'y[23]',
             'y[24]']]  # taking the training data features
        y_train = train.label  # output of our training data
        #X_val = val[
            #['x[0]', 'x[1]', 'x[2]', 'x[3]', 'x[4]', 'x[5]', 'x[6]', 'x[7]', 'x[8]', 'x[9]', 'x[10]', 'x[11]', 'x[12]',
             #'x[13]', 'x[14]', 'x[15]', 'x[16]', 'x[17]', 'x[18]', 'x[19]', 'x[20]', 'x[21]', 'x[22]', 'x[23]', 'x[24]',
             #'y[0]', 'y[1]', 'y[2]', 'y[3]', 'y[4]', 'y[5]', 'y[6]', 'y[7]', 'y[8]', 'y[9]', 'y[10]', 'y[11]', 'y[12]',
             #'y[13]', 'y[14]', 'y[15]', 'y[16]', 'y[17]', 'y[18]', 'y[19]', 'y[20]', 'y[21]', 'y[22]', 'y[23]',
             #'y[24]']]  # taking test data features
        #y_val = val.label  # output value of test data

        X_test = test[
            ['x[0]', 'x[1]', 'x[2]', 'x[3]', 'x[4]', 'x[5]', 'x[6]', 'x[7]', 'x[8]', 'x[9]', 'x[10]', 'x[11]', 'x[12]',
             'x[13]', 'x[14]', 'x[15]', 'x[16]', 'x[17]', 'x[18]', 'x[19]', 'x[20]', 'x[21]', 'x[22]', 'x[23]', 'x[24]',
             'y[0]', 'y[1]', 'y[2]', 'y[3]', 'y[4]', 'y[5]', 'y[6]', 'y[7]', 'y[8]', 'y[9]', 'y[10]', 'y[11]', 'y[12]',
             'y[13]', 'y[14]', 'y[15]', 'y[16]', 'y[17]', 'y[18]', 'y[19]', 'y[20]', 'y[21]', 'y[22]', 'y[23]',
             'y[24]']]  # taking test data features
        y_test = test.label  # output value of test data


        print(X_train.shape)

        print(X_test.shape)
        return X_train, y_train,X_test, y_test
    def modeling(self):
        X_train, y_train,X_test, y_test=self.split()

        model = Sequential()

        model.add(Dense(200, input_dim=50, activation='relu'))
        keras.layers.BatchNormalization()
        model.add(Dense(100, activation='relu'))

        model.add(Dense(5, activation='softmax'))

        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])


        history1 = model.fit(X_train, y_train,batch_size=16, epochs=13,validation_data=(X_test, y_test))
        #test_loss, test_acc = model.evaluate(X_test, y_test)
        #print('테스트 정확도:', test_acc)
        test_loss, test_acc = model.evaluate(X_test, y_test)
        print(f'###############val loss {test_loss}')
        print(f'#################val acc {test_acc}')
        acc = history1.history['accuracy']
        val_acc = history1.history['val_accuracy']
        loss = history1.history['loss']
        val_loss = history1.history['val_loss']
        epochs = range(1, len(loss) + 1)

        plt.plot(epochs, acc, 'b', label='accuracy')
        plt.plot(epochs, val_acc, 'r', label='val_accuracy')
        plt.title('Training and validation')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.show()
        epochs = range(1, len(loss) + 1)
        plt.plot(epochs, loss, 'b', label='Training loss')
        plt.plot(epochs, val_loss, 'r', label='val loss')
        plt.title('Training and validation')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

        file_name = './save/squart_model2.h5'
        model.save(file_name)
        print(f'Model Save in {file_name}')

mmfc_menu = ["Exit",  # 0
               "hook",  # 1
               ]
mmfc_lambda = {
    "1": lambda x: x.modeling(),
}

if __name__ == '__main__':
    MMFC = MMFCModel()

    while True:
        [print(f"{i}. {j}") for i, j in enumerate(mmfc_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                mmfc_lambda[menu](MMFC)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")