import nltk

def pos_tagging(input_string):
    text = nltk.word_tokenize(input_string)
    tagged_list = nltk.pos_tag(text)
    return ['^'.join(ite) for ite in tagged_list]

