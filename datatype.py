class node:
    def __init__(self):
        self.pri=[]
        self.avg_order=0
    def add_pri(pair):
        self.pri.append(pair)
        avg_order=(avg_order*(len(self.pri)-1)+pair[1])/len(self.pri)
    def get_pri():
        return self.pri
    def get_avg_order():
        return self.avg_order


class graph:
    def __init__(self):
        self.nodes={}
    def add_node(string):
        if(string not in self.nodes):
            self.nodes[string]={'node':node(),'next':set(),visited:False}
    def add_edge(string1,string2):
        self.nodes[string1].next.add(string2)
    def get_pri(string):
        return self.nodes[string].node.get_pri()
    def add_pri(string,pair):
        self.nodes[string].node.add_pri(pair)
    def get_avg_order(string):
        return self.nodes[string].node.get_avg_order()
    def get_visited(string):
        return self.nodes[string].visited
    def visit(string):
        self.nodes[string].visited=True
    def unvisit(string):
        self.nodes[string].visited=False
