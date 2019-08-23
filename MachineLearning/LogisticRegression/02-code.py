import math
import random
import csv
import numpy as np

def load_data(path):
    dataset = []
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            dataset.append(row)
    return dataset

def str_to_float(dataset):
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            dataset[i][j] = float(dataset[i][j])
            
def minMaxFinder(dataset):
    minMax = []
    for i in range(len(dataset[0])):
        col = [row[i] for row in dataset]
        min_val = min(col)
        max_val = max(col)
        minMax.append([min_val,max_val])
    return minMax

def normalization(minMax,dataset):
#    x - min(x) / max(x) - min(x)
    for i in range(len(dataset)):
        for j in range(len(dataset[i])):
            x = dataset[i][j]
            min_of_x = minMax[j][0]
            max_of_x = minMax[j][1]
            numer = x - min_of_x
            denom = max_of_x - min_of_x
            dataset[i][j] = numer / denom
            
def crossValidation(dataset,k=5):
    dataset_copy = list(dataset)
    fold_size = len(dataset) // k
    folds = []
    for i in range(k):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        folds.append(fold)
    return folds

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(x,w):
    z = np.dot(x,w)
    return sigmoid(z)

def cost_function(features,target,weights):
    n = len(target)
    y_pred = predict(features,weights)
    cost_1 = -target * np.log(y_pred)
    cost_2 = -(1 - target) * np.log((1 - y_pred))
    cost = cost_1 + cost_2
    total = np.sum(cost) / n
    return total

def gradientDescent(x_train,y_train,epochs,alpha):
    x_train = np.asarray(x_train)
    y_train = np.asarray(y_train)
    w = np.zeros(x_train.shape[1])
    n = len(x_train)
    for epoch in range(epochs):
        pred = predict(x_train,w)
        loss = pred - y_train
        grad = (1/n) * x_train.T.dot(loss)
        w = w - alpha * grad
        if epoch % 1000 == 0:
            print(cost_function(x_train,y_train,w))
    return w

def logistic(x_train,y_train,x_test,y_test,epochs,alpha):
    w = gradientDescent(x_train,y_train,epochs,alpha)
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

def evaluate(dataset,epochs,alpha):
    folds = crossValidation(dataset)
    scores = []
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = np.vstack(train)
        x_train = train[:,:-1]
        y_train = train[:,-1]
        test = list(fold)
        test = np.vstack(test)
        x_test = test[:,:-1]
        y_test = test[:,-1]
        
        pred = logistic(x_train,y_train,x_test,y_test,epochs,alpha)
        s = accuracy(pred,y_test)
        scores.append(s)
    return scores

file = 'diabetes_data.csv'
dataset = load_data(file)
str_to_float(dataset)
minMax = minMaxFinder(dataset)
normalization(minMax, dataset)
#folds = crossValidation(dataset)
epochs = 100000
alpha = 0.3
predictions = evaluate(dataset,epochs,alpha)
print("All accuracies",predictions)
avg = sum(predictions) / len(predictions)
print("Average Accuracy",avg)

