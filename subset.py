import networkx as nx
import numpy as np
from drawGraph import networker

data_path = './selected_edges.csv'

networker = networker(data_path)
# networker.data_loader()
# edges = networker.edges
# networker.build_graph()

def edges2Nodes(networker):
    nodes = []
    [nodes.extend(i) for i in networker.edges]
    nodes = set(nodes)
    networker.nodes = nodes
    

def getAllPath(netwoker, minimalExample=1):

    nodes = list(netwoker.graph.nodes)
    print("The number of nodes is:",len(nodes))
    num = 0
    nodePathNumDic = {}
    for source in nodes:
        num+=1
        if minimalExample:
            if num>2:
                print("The total number that we have handled is:",num-1)
                break
        for target in nodes:
            for path in sorted(nx.all_simple_edge_paths(netwoker.graph,source,target)):
                if len(path) in nodePathNumDic:
                    nodePathNumDic[len(path)]=nodePathNumDic[len(path)]+1
                else:
                    nodePathNumDic[len(path)]=1
    return nodePathNumDic

class Subsets(object):

    def __init__(self,networker):
        self.networker = networker
        self.networker.data_loader()
        self.edges = networker.edges
        self.networker.build_graph()
        edges2Nodes(self.networker)
        nx.write_adjlist(networkHandler.graph,'./adjlist.txt')


    def get_subsets(self, whole_set):
        self.whole_set = whole_set
        output = [[]]
        for i in whole_set:
            output.extend([subset + [i] for subset in output])
        subsets_list = [set(x) for x in output[1:-1]]
        return subsets_list
    def get_path_subedges_set(self,edges,subset):
        '''
        alphas: coefficient list
        '''
        alphas = np.zeros((len(self.whole_set),)).tolist()
        if len(subset)==1:
            return alphas
        else:
            edges_subset = []
            for i in edges:
                if i[0] in subset and i[1] in subset:
                    edges_subset.append(i)
            if len(edges_subset)==0:
                return alphas
            else:
                self.networker.edges = edges_subset
                self.networker.build_graph()
                edges2Nodes(self.networker)
                pathDict = getAllPath(self.networker)
                for i in range(len(subset)):
                    alphas[i] = pathDict.get(i,0)
                return alphas
    def get_listOfAlphas(self,edges,whole_set):
        subsets_list = self.get_subsets(whole_set)
        alphas_list = []
        for i in subsets_list:
            alphas_list.append(self.get_path_subedges_set(edges,i))
        return subsets_list,alphas_list




            

if __name__ == "__main__":

    whole_set = [1,2,3]
    subsets = Subsets(networker)
    subsets_list = subsets.get_subsets(whole_set)
    print(subsets_list)

    # whole_set = nx.nodes(networker.graph)
    # print(whole_set)
    # subsets = Subsets()
    # subsets_list = subsets.get_subsets(whole_set)
    # print(subsets_list)

