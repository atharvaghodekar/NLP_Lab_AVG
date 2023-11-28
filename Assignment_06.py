# Name: Atharva Vinod Ghodekar
# Batch: B2
# Roll no: 23
# Pract no. 6: Dependency parsing using spacy

import spacy
from spacy import displacy
import en_core_web_sm
nlp = en_core_web_sm.load()
piano_text = "Atharva is learning pyano"
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
    
displacy.serve(piano_doc, style="dep")
    
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