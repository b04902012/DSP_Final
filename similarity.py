def similarity(path1,path2): 
    set1=set(path1)
    set2=set(path2)
    return float(len(set1&set2)/len(set1|set2))
