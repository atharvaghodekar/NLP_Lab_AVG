# Assignment No 6
# Name - Atharva Ghodekar
# Batch - B2
# Roll No - 23
# Assignment Title : Implement and visualize Dependency Parsing of Textual Input using Standford CoreNLP and Spacy library

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
Atharva is python developer 
He is working on NLP project
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")

# OUTPUT -
# TOKEN: 

# =====
# token.tag_ = '_SP'
# token.head.text = 'Atharva'
# token.dep_ = 'dep'

# TOKEN: Atharva
# =====
# token.tag_ = 'NNP'
# token.head.text = 'is'
# token.dep_ = 'nsubj'

# TOKEN: is
# =====
# token.tag_ = 'VBZ'
# token.head.text = 'is'
# token.dep_ = 'ROOT'

# TOKEN: python
# =====
# token.tag_ = 'NNP'
# token.head.text = 'developer'
# token.dep_ = 'compound'

# TOKEN: developer
# =====
# token.tag_ = 'NN'
# token.head.text = 'is'
# token.dep_ = 'attr'

# TOKEN:

# =====
# token.tag_ = '_SP'
# token.head.text = 'developer'
# token.dep_ = 'dep'

# TOKEN: He
# =====
# token.tag_ = 'PRP'
# token.head.text = 'working'
# token.dep_ = 'nsubj'

# TOKEN: is
# =====
# token.tag_ = 'VBZ'
# token.head.text = 'working'
# token.dep_ = 'aux'

# TOKEN: working
# =====
# token.tag_ = 'VBG'
# token.head.text = 'developer'
# token.dep_ = 'relcl'

# TOKEN: on
# =====
# token.tag_ = 'IN'
# token.head.text = 'working'
# token.dep_ = 'prep'

# TOKEN: NLP
# =====
# token.tag_ = 'NNP'
# token.head.text = 'project'
# token.dep_ = 'compound'

# TOKEN: project
# =====
# token.tag_ = 'NN'
# token.head.text = 'on'
# token.dep_ = 'pobj'

# TOKEN:

# =====
# token.tag_ = '_SP'
# token.head.text = 'project'
# token.dep_ = 'dep'

# Using the 'dep' visualizer
# Serving on http://0.0.0.0:5000 ...
