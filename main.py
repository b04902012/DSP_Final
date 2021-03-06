from IPython import embed
import sys
node=__import__('datatype').node
graph=__import__('datatype').graph
graphize=__import__('graphizer').graphize
pos_tagging=__import__('POS_tagging').pos_tagging
traversal=__import__('traversal').traversal
scoring_simple=__import__('scoring').scoring_simple
output=__import__('output').output


sentences=open(sys.argv[1],mode='rt').read().split('\n')[0:-1]
tagged_sentences=[]

frequency_threshold=max(len(sentences)//100,1)
word_count={}

for i in range(0,len(sentences)):
    tagged_sentences.append(pos_tagging(sentences[i]))
    appeared=[]
    for word in tagged_sentences[i]:
        if(word not in word_count):
            word_count[word]=0
        if(word not in appeared):
            word_count[word]=word_count[word]+1
            appeared.append(word)

g=graphize(tagged_sentences,word_count)

path_list=traversal(g,frequency_threshold)
print("!!!!!!!!!!!!!!!!!!")
path_score_list=[]
for p in path_list:
    path_score_list.append((p,scoring_simple(g,p)))
print(output(path_score_list,3,0.5))

