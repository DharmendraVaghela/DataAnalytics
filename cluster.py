import pandas as pd
from yelp import *
import nltk
import os
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from pandas import DataFrame
import matplotlib.pyplot as plt
import pickle

bid='4bEjOyTaDG24SY5TxsaUNQ'
stemmer=nltk.PorterStemmer()
def get_business_json_string(bid):
    f=open('../Dataset/business.json')
    x=f.readline()
    while bid not in x:
        x=f.readline()
    f.close()
    return x

def stem_tokens(tokens,stemmer):
    stemmed=[]
    for token in tokens:
        stemmed.append(stemmer.stem(token))
    return stemmed

def tokenize(text):
    tokens=nltk.word_tokenize(text)
    stems=stem_tokens(tokens,stemmer)
    return stems

def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens




json_business_text=get_business_json_string(bid)
b1=YelpBusiness.parse_json(json_business_text)
print 'Name:',b1.name
dataset=b1.update_review_data()

totalvocab_stemmed = []
totalvocab_tokenized = []
for i in dataset.keys():
    allwords_stemmed = tokenize_and_stem(dataset[i]) #for each item in 'synopses', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
    
    allwords_tokenized = tokenize_only(dataset[i])
    totalvocab_tokenized.extend(allwords_tokenized)

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print 'there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame'

print vocab_frame.head()
tfidf_vectorizer=TfidfVectorizer(tokenizer=tokenize,stop_words="english",use_idf=True)
model=tfidf_vectorizer.fit_transform(dataset.values())
terms=tfidf_vectorizer.get_feature_names()
num_of_clusters=50

kmeans_executor=KMeans(n_clusters=num_of_clusters)
kmeans_executor.fit(model)

from sklearn.externals import joblib

joblib.dump(kmeans_executor,'kmeans_model.pkl')

clusters = kmeans_executor.labels_.tolist()


data=zip(dataset.keys(),clusters)
frame=DataFrame(data,columns=['ReviewLineId','Cluster'])

print"Top terms per cluster:"
print 
#sort cluster centers by proximity to centroid
order_centroids = kmeans_executor.cluster_centers_.argsort()[:, ::-1] 

for i in range(num_of_clusters):
    "Cluster %d words:" % i,
    
    for ind in order_centroids[i, :10]: #replace 6 with n words per cluster
        try:
            print ' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore')
        except:
            pass
    print #add whitespace
    print #add whitespace
    print "Cluster %d titles:" % i
    for title in frame[frame['Cluster']==i]['ReviewLineId'][:10]:
        print' %s,' % title,dataset[title]
    print #add whitespace
    print #add whitespace
    
print
print
