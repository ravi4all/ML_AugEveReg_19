import math
import random
import csv

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

file = 'diabetes_data.csv'
dataset = load_data(file)
str_to_float(dataset)
minMax = minMaxFinder(dataset)
normalization(minMax, dataset)
