import spacy

nlp = spacy.load("en_core_web_sm")

with open("data/wiki_us.txt", "r") as file:
    text = file.read()
# print(text)

doc = nlp(text)
# print(doc)

# print(len(text))
# print(len(doc))

# for token in text[0:10]:
#     print(token)
    
# for token in doc[0:10]:
#     print(token)
    
# for token in text.split()[:10]:
#     print(token)
    
# for sent in doc.sents:
    # print(sent)
    
sentence1 = list(doc.sents)[0]
# print(sentence1)

# for token in doc[:10]:
    # print(token)
    
token2 = sentence1[2]
print(token2)

# print(token2.text)
print(token2.left_edge)
print(token2.right_edge)
print(token2.ent_type)
print(token2.ent_type_)
print(token2.ent_iob_)
print(token2.lemma_)
print(sentence1[12].lemma_)
print(sentence1[12])
print(token2.morph) # what a word is morphologically
print(sentence1[12].morph)
print(token2.pos_) # part of speech
print(token2.dep_) # noun subject
print(token2.lang_)