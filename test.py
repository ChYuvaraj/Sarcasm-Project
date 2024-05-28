from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from string import punctuation
from nltk.corpus import stopwords

def clean_doc(doc):
    tokens = doc.split()
    table = str.maketrans('', '', punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    tokens = [word for word in tokens if len(word) > 1]
    tokens = ' '.join(tokens) #here upto for word based
    return tokens

def getCount(sentence):
    pos = []
    neg = []
    neu = []
    arr = sentence.split(' ')
    for i in range(len(arr)):
        word = arr[i].strip()
        if (sid.polarity_scores(word)['compound']) >= 0.1:
            pos.append(word)
        elif (sid.polarity_scores(word)['compound']) <= -0.1:
            neg.append(word)
        else:
            neu.append(word)
    return pos,neg,neu      


#sentence = 'Mark Zuckerberg used to be a hero of the digital age, but now he has lived long enough to see himself become the villain'
#sentence = 'I love it when the bus smells like cat piss and dirty laundry'
#sentence = 'sometimes its better to lose an argument than lose someone you love'
#sentence = 'I dont think you are a fool but what my opinion in compare to that of thousands of others'
sentence = 'I never forget a face, but in your case I will be glad to make an exception'
sentence = clean_doc(sentence)
sid = SentimentIntensityAnalyzer()

sentiment_dict = sid.polarity_scores(sentence)
print(sentiment_dict)
compound = sentiment_dict['compound']
result = ''
if compound >= 0.1 :
    result = 'Positive' 
elif compound <= -0.1:
    result = 'Negative' 
else :
    result = 'Neutral'

pos,neg,neu = getCount(sentence)
print(pos)
print(neg)
print(neu)
print(str(len(pos))+" "+str(len(neg))+" "+str(len(neu)))
print(result)
