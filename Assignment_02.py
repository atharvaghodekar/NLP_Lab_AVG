#Assignment no : 2
#Name : Atharva Vinod Ghodekar
#Batch : B2
#Roll no : 23
#Title : Natural Language Processing (NLP) using Gensim

import gensim
from gensim import corpora

text1 = ["My name is Atharva Ghodekar.", 
   "I am from Sanjivani College of Engineering.", 
   "Atharva is from Ahmednagar. "]


tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

#Output :
#The dictionary has: 13 tokens
#{'Atharva': 0, 'Ghodekar.': 1, 'My': 2, 'is': 3, 'name': 4, 'College': 5, 'Engineering.': 6, 'I': 7, 'Sanjivani': 8, 'am': 9, 'from': 10, 'of': 11, 'Ahmednagar.': 12}
#Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], [(5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1)], [(0, 1), (3, 1), (10, 1), (12, 1)]]
