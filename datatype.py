class node:
    def __init__(self):
        self.pri=[]
        self.avg_order=0
    def add_pri(self,pair):
        self.pri.append(pair)
        self.avg_order=(self.avg_order*(len(self.pri)-1)+pair[1])/len(self.pri)
    def get_pri(self):
        return self.pri
    def get_avg_order(self):
        return self.avg_order


class graph:
    def __init__(self):
        self.nodes={}
    def add_node(self,string):
        if(string not in self.nodes):
            self.nodes[string]={'node':node(),'next':set(),'visited':False}
    def add_edge(self,string1,string2):
        self.nodes[string1]['next'].add(string2)
    def get_pri(self,string):
        return self.nodes[string]['node'].get_pri()
    def add_pri(self,string,pair):
        self.nodes[string]['node'].add_pri(pair)
    def get_avg_order(self,string):
        return self.nodes[string]['node'].get_avg_order()
    def get_visited(self,string):
        return self.nodes[string]['visited']
    def visit(self,string):
        self.nodes[string]['visited']=True
    def unvisit(self,string):
        self.nodes[string]['visited']=False
