# Name: Abhijit Balasaheb Phapale
# Batch: B3
# Roll no: 45
# Pract no. 6: Dependency parsing using spacy

import spacy
nlp = spacy.load("en_core_web_sm")
piano_text = "Atharva is learning piano"
piano_doc = nlp(piano_text)
for token in piano_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )
    
# Output:
# TOKEN: Atharva
# =====
# token.tag_ = 'NNP'
# token.head.text = 'learning'
# token.dep_ = 'nsubj'

# TOKEN: is
# =====
# token.tag_ = 'VBZ'
# token.head.text = 'learning'
# token.dep_ = 'aux'

# TOKEN: learning
# =====
# token.tag_ = 'VBG'
# token.head.text = 'learning'
# token.dep_ = 'ROOT'

# TOKEN: piano
# =====
# token.tag_ = 'NN'
# token.head.text = 'learning'
# token.dep_ = 'dobj'