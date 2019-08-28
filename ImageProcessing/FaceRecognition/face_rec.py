import numpy as np
import pickle
import cv2

face_1 = np.load('face_1.npy')
face_2 = np.load('face_2.npy')

# data previous shape - 200,50,50
face_1 = face_1.reshape(200,-1)
# after reshape - 200,2500
face_2 = face_2.reshape(200,-1)

faces = np.concatenate([face_1,face_2])

faces = faces/255.

labels = np.zeros((faces.shape[0],1))
labels[200:,:] = 1.0

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(x,w):
    z = np.dot(x,w)
    return sigmoid(z)

def gradientDescent(x_train,y_train,epochs,alpha):
    w = np.zeros(x_train.shape[1])
    n = len(x_train)
    for epoch in range(epochs):
        pred = predict(x_train,w)
        loss = pred - y_train.flatten()
        grad = (1/n) * x_train.T.dot(loss)
        w = w - alpha * grad
    return w

def logistic(x_train,y_train,epochs,alpha):
    w = gradientDescent(x_train,y_train,epochs,alpha)
    file = open('weights.pkl','wb')
    pickle.dump(w,file)
    prediction = predict(x_train,w)
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
    pred = logistic(faces, labels,epochs, alpha)
    s = accuracy(pred, labels)
    return s

epochs = 100000
alpha = 0.01
score = evaluate(epochs,alpha)
print(score)