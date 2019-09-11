from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import pickle

def textProcessing(df):
    myStopwords = [',','...','?','.']
    s = stopwords.words('english')
    s.extend(myStopwords)
    wordList = []
    for i in range(len(df)):
        t = word_tokenize(df['Review'].iloc[i].lower())
        wordList.append(t)
        
    words = []
    for itemList in wordList:
        wordList = []
        for word in itemList:
            if word not in s:
                wordList.append(word)
        words.append(wordList)
        
    wnet = WordNetLemmatizer()
    for i in range(len(words)):
        for j in range(len(words[i])):
            words[i][j] = wnet.lemmatize(words[i][j],pos='v')
            
    for i in range(len(words)):
        words[i] = ' '.join(words[i])
    
    return words

def test(review):
    file = open('vec.pkl','rb')
    cv = pickle.load(file)
    file.close()
    file = open('reg.pkl','rb')
    reg = pickle.load(file)
    df = pd.DataFrame({"Review":[review]})
    words = textProcessing(df)
    vec = cv.transform(words)
    pred = reg.predict(vec)
    return pred[0]