import spacy
nlp = spacy.load("en_core_web_sm")
        
#Tokenization
print("\nTokenization :-")
about_text = (
    "Atharva is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
    )
about_doc = nlp(about_text)

for token in about_doc:
  print (token, token.idx)
  
#Stop words  
print("\nStop words :-") 
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)
    custom_about_text = (
    "Atharva is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
    )
about_doc = nlp(custom_about_text)
print([token for token in about_doc if not token.is_stop])

#Lemmatization
print("\nLemmatization :-")
conference_help_text = (
    "Atharva is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
    )
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


#Part of Speech
print("\nPart of Speech :-")
about_text = (
    "Atharva is a Python developer currently"
    " working for a London-based Fintech"
    " company. He is interested in learning"
    " Natural Language Processing."
    )
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )

# Output :
# Tokenization :-
# Atharva 0
# is 8
# a 11
# Python 13
# developer 20
# currently 30
# working 40
# for 48
# a 52
# London 54
# - 60
# based 61
# Fintech 67
# company 75
# . 82
# He 84
# is 87
# interested 90
# in 101
# learning 104
# Natural 113
# Language 121
# Processing 130
# . 140

# Stop words :-
# through
# nowhere
# 've
# per
# sometime
# already
# thru
# less
# because
# thereby
# [Atharva, Python, developer, currently, working, London, -, based, Fintech, company, ., interested, learning, Natural, Language, Processing, .]

# Lemmatization :-
#                   is : be
#              working : work
#                based : base
#                   He : he
#                   is : be
#             learning : learn

# Part of Speech :-

# TOKEN: Atharva
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: is
# =====
# TAG: VBZ        POS: AUX
# EXPLANATION: verb, 3rd person singular present

# TOKEN: a
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: Python
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: developer
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: currently
# =====
# TAG: RB         POS: ADV
# EXPLANATION: adverb

# TOKEN: working
# =====
# TAG: VBG        POS: VERB
# EXPLANATION: verb, gerund or present participle

# TOKEN: for
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: a
# =====
# TAG: DT         POS: DET
# EXPLANATION: determiner

# TOKEN: London
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: -
# =====
# TAG: HYPH       POS: PUNCT
# EXPLANATION: punctuation mark, hyphen

# TOKEN: based
# =====
# TAG: VBN        POS: VERB
# EXPLANATION: verb, past participle

# TOKEN: Fintech
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: company
# =====
# TAG: NN         POS: NOUN
# EXPLANATION: noun, singular or mass

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer

# TOKEN: He
# =====
# TAG: PRP        POS: PRON
# EXPLANATION: pronoun, personal

# TOKEN: is
# =====
# TAG: VBZ        POS: AUX
# EXPLANATION: verb, 3rd person singular present

# TOKEN: interested
# =====
# TAG: JJ         POS: ADJ
# EXPLANATION: adjective (English), other noun-modifier (Chinese)

# TOKEN: in
# =====
# TAG: IN         POS: ADP
# EXPLANATION: conjunction, subordinating or preposition

# TOKEN: learning
# =====
# TAG: VBG        POS: VERB
# EXPLANATION: verb, gerund or present participle

# TOKEN: Natural
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: Language
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: Processing
# =====
# TAG: NNP        POS: PROPN
# EXPLANATION: noun, proper singular

# TOKEN: .
# =====
# TAG: .          POS: PUNCT
# EXPLANATION: punctuation mark, sentence closer
