datatype=__import__('datatype')
node=datatype.node
graph=datatype.graph
def graphize(sentences,word_count,frequency_threshold):
    g=graph()
    for sid in range(0,len(sentences)):
        sentence=sentences[sid]
        for wid in range(0,len(sentence)):
            word=sentence[wid]
            if(word_count[word]<frequency_threshold):
                continue
            g.add_node(word)
            g.add_pri(word,(sid,wid))
            if(wid>0):
                if(word_count[sentence[wid-1]]>=frequency_threshold):
                    g.add_edge(sentence[wid-1],word)
        
    return g
