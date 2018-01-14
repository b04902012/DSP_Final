datatype = __import__('datatype')
node = datatype.node
graph = datatype.graph

def end_node(g,s): #g = graph, s = node string
    punctuation_list = [",", "!", ".", "?", ";"]
    if s.split('^')[0] in punctuation_list:
        return true
    if s.split('^')[1] == "CC":
        return true
    return false

