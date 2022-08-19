from nltk.corpus import wordnet

synonyms = []

for syn in wordnet.synsets("name"):
    for lm in syn.lemmas():
             synonyms.append(lm.name())
print (set(synonyms))