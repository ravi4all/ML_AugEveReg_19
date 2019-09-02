import numpy as np
import pickle
from sklearn.model_selection import train_test_split

data = np.load('data.npy')
labels = np.load('labels.npy')

data = data.reshape(data.shape[0], -1)

# print(data.shape, labels.shape)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(x,w):
    z = np.dot(x,w)
    return sigmoid(z)

def gradientDescent(x_train,y_train,epochs,alpha):
    w = np.zeros(x_train.shape[1])
    n = len(x_train)
    for epoch in range(epochs):
        print(epoch)
        pred = predict(x_train,w)
        loss = pred - y_train.flatten()
        grad = (1/n) * x_train.T.dot(loss)
        w = w - alpha * grad
    return w

def logistic(x_train,y_train,x_test,epochs,alpha):
    w = gradientDescent(x_train,y_train,epochs,alpha)
    file = open('weights.pkl','wb')
    pickle.dump(w,file)
    prediction = predict(x_test,w)
    for i in range(len(prediction)):
        prediction[i] = round(prediction[i])
    return prediction

def accuracy(predictions,actual):
    count = 0
    for i in range(len(predictions)):
        if predictions[i] == actual[i]:
            count += 1
    return count / len(predictions) * 100

def evaluate(epochs, alpha):
    x_train,x_test,y_train,y_test = train_test_split(data,labels,test_size=0.25)
    y_pred = logistic(x_train,y_train,x_test,epochs, alpha)
    s = accuracy(y_pred, y_test)
    return s

epochs = 1000
alpha = 0.001
score = evaluate(epochs,alpha)
print(score)
