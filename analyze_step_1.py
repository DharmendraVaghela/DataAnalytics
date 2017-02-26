import os
import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist
from nltk.corpus import stopwords

def build_corpus(category_name):
    '''
        Parses the review documents for a particular category and returns a corpus.
        The location of the directory is hardcoded where these documents are to be searched.
    '''
    print 'Building corpus of category name: %s'%category_name
    root=os.path.join('../CategorizedJSON','dir_category_'+category_name.replace(' ','_').replace('/','_'))
    reader=PlaintextCorpusReader(root,'.*\.txt')
    return reader

def get_filtered_corpus_text(reader):
    '''
        Removes the stopwords and non alphanumeric words from the word list.
        All words are converted into lower case.
    '''
    print 'Removing the stopwords and non alphanumeric words and converting all words into lowercase'
    s=stopwords.words()
    all_words=reader.words()
    t=nltk.Text(w.lower() for w in all_words if w.lower() not in s and w.isalnum())
    return t     

def plot_freq_dist(text,top_x=50):
    '''
        Plots the frequency distribution of top "top_x" words in the text instance.
    '''
    print 'Computing and plotting the frequency distribution for top %d words in the text'%top_x
    fd=FreqDist(text)
    fd.plot(top_x)

def get_corpus_statistics(corpus):
    '''
        Computes some simple statistics for a given corpus like no. of words, no. of unique words,sentences etc.
    '''
    words=len(corpus.words())
    sentences=len(corpus.sents())
    characters=len(corpus.raw())
    unique_words=len(set(w.lower() for w  in corpus.words() if w.isalnum()))
    number_of_files=len(corpus.fileids())
    print 'No. of documents is',number_of_files
    print 'No. of characters is',characters
    print 'No. of sentences is',sentences
    print 'No .of words is',words
    print 'No. of unique words is',unique_words
  
    
def main():
    corpus= build_corpus('Indian')
    #print 'Indian Restaturant Corpus Statistics'
    #get_corpus_statistics(corpus)
    indian_text=get_filtered_corpus_text(corpus)
    plot_freq_dist(indian_text)
    
if __name__ == "__main__":
    main()
