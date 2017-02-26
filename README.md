# DataAnalytics
Customer Reviews Analysis for any Business 


1. Background


Problem:

On yelp website people post reviews on different businesses. These reviews are accumulated over the time and resulted in a huge chunk of data from which no meaningful information can be derived on its own. For high-dimensional data such as reviews, it is difficult to extract prominent features. However, data in this form have certain simple structure which can be transformed to get the meaningful information. For example, reviews might contain information about ambience, staff service, food quality etc. in case of restaurant business. Our goal is to mine relevant parameters from the set of reviews and inform the business about what their customers think of  their services the most. This information will guide business to improve the aspects that are most relevant to their customers which in turn affect the revenue of particular business.

Literature Survey:

In Yelp dataset challenge, many approaches applied in the direction to improve the business. Latent Semantic Indexing (LSI) is among the most basic and well-known technique used in dimentionality reduction. LSI faced several issues due
to the formulation of the probabilistic model and Probabilistic Latent Semantic Indexing (PLSI) came up as a solution. But even PLSI has problem of over fitting when dealing with small dataset. Our approach will not face problem of over fitting and can deal with any size of data. In another approach by James Huang, Stephanie Rogers, Eunkwang Joo, reviews are broken down into latent subtopics using LDA and then team can predict the star rating for derived hidden subtopic[Reference paper]. Ultimately these ratings per hidden topic can pinpoint the reasons for a restaurant’s Yelp rating. There are primarily two shortcoming of this work. First, It only deals with restaurant as a business. No other business is considered on which this model can be applied. Our project can accommodate any business in given dataset and predict the subtopic which is most relevant to the business. Second, it only predicts the star rating for given review subtopic which increases the chance of ignoring the most relevant subtopic if star rating is does not fit the probabilistic model. We used clustering algorithms to group contextually similar parameters of the obtained bag of words model which allow business owner to easily reconcile the voice of hi/her customer base irrespective of the star rating.

2. Proposed method

Approach:

A. Dataset: 

This research is performed with the data from the Yelp Dataset Challenge. This dataset includes business, review, user, and checkin data in the form of separate JSON objects. A business object includes information about the type of business, location, rating, categories, and business name, as well as contains a unique id. A review object has a rating, review text, and is associated with a specific business id and user id. We used two types of JSON data Business ID and associated review. We first divide all businesses in different category and derive the list of reviews for given category. By this we can apply our model to any business category.

B. Breaking reviews into sentences

In this step, each review is broken down into sentences by "." , "?" or "and". This sentences will work as a separate entity to determine the weight for the next step.

C. [Stopwords??], Stemming and Tokenization

Tokenization is the process of breaking a stream of text up into words, phrases, symbols, or other meaningful elements called tokens. The list of tokens becomes input for further processing such as clustering.[https://en.wikipedia.org/wiki/Tokenization_(lexical_analysis)] 
Stemming is the process for reducing inflected (or sometimes derived) words to their word stem, base or root form—generally a written word form. The stem need not be identical to the morphological root of the word; it is usually sufficient that related words map to the same stem, even if this stem is not in itself a valid root.[ https://en.wikipedia.org/wiki/Stemming]

For each review, we have broken down the contents in sentences in order to get tokens. First tokenization and stemming is done on the sentences and then by word to ensure that punctuation is caught as token. These token will serve as an input for transforming into vector space. We have used two first, functions tokenize_and_stem: this will stem the tokens and provide stemmed output. Second tokenize_only: this will only do tokenization without stemming. By this approach, we will create a dictionary which becomes available when conversion from tokens to sentences is  required at the time of result display.

D. Transforming the corpus into vector space

From dataframe of tokens, we use tf-idf to convert into vector space. tf–idf(term frequency–inverse document frequency) is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. It is often used as a weighting factor in information retrieval and text mining. The tf-idf value increases proportionally to the number of times a word appears in the document, but is offset by the frequency of the word in the corpus, which helps to adjust for the fact that some words appear more frequently in general. Term frequency: The weight of a term that occurs in a document is simply proportional to the term frequency while Inverse document frequency : It is a measure of how much information the word provides, that is, whether the term is common or rare across all documents. These two factors are multiplied together in order to diminish the effect of most frequent words and increase the weight of rare words.
Here we defined term frequency-inverse document frequency (tf-idf) vectorizer parameters and then convert the dataset values into a tf-idf matrix. While converting into tf-idf vector stopwords will be excluded from consideration. Feature names will be derived from the vector space matrix.

E. K-means clustering:

k-means clustering is a method of vector quantization which aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean, serving as a prototype of the cluster. K-means converges to centers minimizing the sum of squared centerpoint distances. Next, the mean of the clustered observations is calculated and used as the new cluster centroid. Then, observations are reassigned to clusters and centroids recalculated in an iterative process until the algorithm reaches convergence. K-means takes pre-determined number of clusters. Here we took 50 as number of clusters. Input for K-means is the tf-idf matrix we derived in the previous step.

F. Tools:
We have implemented the project in python with libraries such as NLTK, Scikit-Learn and Pandas.


G. Model Example:


Rationale:

We have used tf-idf to transform dataset into vector space. Latent semantic analysis(LSA) is an alternative approach which also derive vector space matrix containing word counts per paragraph which is constructed from a large piece of text comparing similar words that occurs in the text. LSA will only applicable for the text which is divided into paragraph and then relationship between paragraph need to be determine. In our project, we have to derive common result from all given review in the dataset therefore we have to consider all review as a chunk of data for particular business. So tf-idf is more suitable approach for vector space matrix.


3. Plan

Hypotheses: 

Feedback is essential for business improvement. Reviews on the Yelp website not only guide people in making informed choices for their needs but also provide a feedback mechanism for businesses to help them improve. Efforts will be made to mine quality parameters relevant for different businesses from the corpus of review documents using natural language processing tools and machine learning algorithms. The obtained parameters will represent important aspects of businesses affecting people. Clustering of important parameters will give important information about where should the business owner focus on. Our project is aimed to achieve this objective with clustering the reviews for given business model.

New Hypothesis:

This project aim to identify the most relevant feature of reviews given by customers for any given business. Customers give reviews and share their opinion about the business in assorted manner. Collection of all these reviews will not give any fruitful information to the business owner about what is the most important aspect. If a business owner need to improve any feature of the business, it is hard to find out customer choice from assorted reviews. Our project goal is to derive meaningful information and topics from dataset and provide useful information to the business owner about their customer's thinking. In general, most relevant feature from collective reviews will be filtered out in the form of clusters.


Experimental Design:

While developing the project, there were number of design issues. First, a small number for clusters were used while applying K-Means algorithm on the dataset. But that approach gave very generic clusters because of grouping of clusters into one big cluster. By gradually increasing the size of number of clusters, meaningful clusters are derived. 

Second, 

Second, while using tf-idf we first thought not to use inverse document frequency while developing  vector matrix but that gave us clusters with trivial dataset. So we incorporated idf in order to get meaningful clusters.

Future Planning:
In this project, K-Means algorithm was used for clustering. It is observed that similar meaning clusters can be clubbed together in order to provide better clustering. This can be achieved by running semantic analysis on the dataset and merge similar meaning clusters using Hierarchical Clustering.


4. Experiments:

4a. Results:
4b. Critical Evaluation:

5. Conclusions:




