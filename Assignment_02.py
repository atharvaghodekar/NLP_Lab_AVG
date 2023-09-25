#Assignment no : 1
#Name : Atharva Vinod Ghodekar
#Batch : B2
#Roll no : 23
#Title : 

import gensim
import pprint
from gensim import corpora
from gensim.utils import simple_preprocess

doc_list = [
   "My name is Atharva Ghodekar.", 
   "I am from Sanjivani College of Engineering.", 
   "Atharva is from Ahmednagar. "
]

doc_tokenized = [simple_preprocess(doc) for doc in doc_list]
dictionary = corpora.Dictionary()
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
BoW_corpus = [dictionary.doc2bow(doc, allow_update=True) for doc in doc_tokenized]
print(BoW_corpus)
print("--------------------------------------------------------------------------------------------------------")
id_words = [[(dictionary[id], count) for id, count in line] for line in BoW_corpus]
print(id_words)
