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
for i in range(0,len(sentences)):
    tagged_sentences.append(pos_tagging(sentences[i]))
g=graphize(tagged_sentences)


path_list=traversal(g)
path_score_list=[]
for p in path_list:
    path_score_list.append((p,scoring_simple(g,p)))
print(output(path_score_list,3,1))

