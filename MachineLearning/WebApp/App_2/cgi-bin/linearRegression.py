import pickle as pkl

file = open('weights.pkl','rb')
reg = pkl.load(file)
file.close()

file = open('onhot.pkl','rb')
onehot = pkl.load(file)
file.close()

file = open('scaling.pkl','rb')
sc = pkl.load(file)
file.close()

def test(gender,per10,per12,tier,degree,gpa,english,logical,quant):
    newData = [[gender,per10,per12,tier,degree,gpa,english,logical,quant]]
    newData = onehot.transform(newData)
    pred = reg.predict(newData)
    pred = sc.inverse_transform(pred)
    return round(pred[0][0])