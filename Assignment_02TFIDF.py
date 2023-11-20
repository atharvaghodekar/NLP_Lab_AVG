#Assignment no : 2
#Name : Atharva Ghodekarr
#Batch : B2
#Roll no : 23
#Title : Natural Language Processing (NLP) using Gensim (TFIDF)

import gensim
from gensim import corpora
from gensim.utils import simple_preprocess
from gensim import corpora


text = ["My name is Atharva Ghodekar.", 
   "I am from Sanjivani College of Engineering.", 
   "Atharva is from Ahmednagar. "]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])

#Output :
#Dictionary : 
#[['atharva', 1], ['ghodekar', 1], ['is', 1], ['my', 1], ['name', 1]]
#[['am', 1], ['college', 1], ['engineering', 1], ['from', 1], ['of', 1], ['sanjivani', 1]]
#[['atharva', 1], ['is', 1], ['from', 1], ['ahmednagar', 1]]
