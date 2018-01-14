datatype=__import__('datatype')
node=datatype.node
graph=datatype.graph
start_node=__import__('start_node').start_node
end_node=__import__('end_node').end_node
def valid(g,s,t):
    return start_node(g,s,t) and end_node(g,s)
