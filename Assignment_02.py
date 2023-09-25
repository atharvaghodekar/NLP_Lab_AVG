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

#Output :
#[[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], [(5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1)], [(0, 1), (2, 1), (8, 1), (11, 1)]]
#--------------------------------------------------------------------------------------------------------
#[[('atharva', 1), ('ghodekar', 1), ('is', 1), ('my', 1), ('name', 1)], [('am', 1), ('college', 1), ('engineering', 1), ('from', 1), ('of', 1), ('sanjivani', 1)], [('atharva', 1), ('is', 1), ('from', 1), ('ahmednagar', 1)]]
