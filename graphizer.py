datatype=__import__('datatype')
node=datatype.node
graph=datatype.graph
def graphize(sentences,word_count):
    g=graph()
    for sid in range(0,len(sentences)):
        sentence=sentences[sid]
        for wid in range(0,len(sentence)):
            word=sentence[wid]
            g.add_node(word)
            g.add_pri(word,(sid,wid))
            if(wid>0):
                g.add_edge(sentence[wid-1],word)
        
    return g
