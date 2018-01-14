class node:
    def __init__(self):
        self.pri=[]
    def add_pri(pair):
        self.pri.append(pair)
    def get_pri():
        return self.pri


class graph:
    def __init__(self):
        self.nodes={}
    def add_node(string):
        if(string not in self.nodes):
            self.nodes[string]={'node':node(),'next':set()}
    def add_edge(string1,string2):
        self.nodes[string1].next.add(string2)
    def get_pri(string):
        return self.nodes[string].node.get_pri()
    def add_pri(string,pair):
        self.nodes[string].node.add_pri(pair)
