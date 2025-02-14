"""
A sample of convert the cifar100 dataset to 224 * 224 size train\val data.
"""
import cv2
import os
import pickle
import numpy
#from keras.datasets import cifar100

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo)
    return dict


def convert():
    train = 'train//'
    val = 'validation//'
    #(X_train, y_train), (X_test, y_test) = cifar100.load_data(label_mode='fine')
    dict1=unpickle('/home/usr1/Env/MobilenetV2/data/train_data')
    dict2=unpickle('/home/usr1/Env/MobilenetV2/data/test_data')
    
    X_train=dict1['data']
    y_train=numpy.asarray(dict1['labels'])
    
    
    X_test=dict2['data']
    y_test=numpy.asarray(dict2['labels'])

'''
    for i in range(len(X_train)):
        x = X_train[i]
        y = y_train[i]
        path = train + str(y[0])
        x = cv2.resize(x, (224, 224), interpolation=cv2.INTER_CUBIC)
        if not os.path.exists(path):
            os.makedirs(path)
        cv2.imwrite(path + '//' + str(i) + '.jpg', x)

    for i in range(len(X_test)):
        x = X_test[i]
        y = y_test[i]
        path = val + str(y[0])
        x = cv2.resize(x, (224, 224), interpolation=cv2.INTER_CUBIC)
        if not os.path.exists(path):
            os.makedirs(path)
        cv2.imwrite(path + '//' + str(i) + '.jpg', x)
'''

if __name__ == '__main__':
    convert()
