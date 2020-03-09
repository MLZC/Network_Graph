#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

data_path = './selected_edges.csv'

class nextworker(object):
    def __init__(self,data_path):
        self.data_path = data_path
        self.edges = None
        self.graph = None
    def data_loader(self):
        csv_data=pd.read_csv(self.data_path)
        source=np.array(csv_data['Source']).reshape(-1,1)
        target=np.array(csv_data['Target']).reshape(-1,1)
        edges=np.concatenate((source,target),axis=1)
        nextworker.edges = edges
    def build_graph(self):
        G=nx.Graph()
        G.add_edges_from(self.edges)
        self.graph = G

    def get_graph_details(self):
        print("The Graph has %d number of nodes!" % self.graph.number_of_nodes())
        print("The Graph has %d number of edges!" % self.graph.number_of_edges())
        print("The Graph has %d number of selfloops!" % self.graph.number_of_selfloops())

    def visualize_network(self):
        pos=nx.random_layout(self.graph)
        nx.draw(self.graph, pos=pos,with_labels=True)
        plt.savefig("Graph.png")
        plt.show()
    def get_rank_of_nodes(self):
        degree_rank = nx.degree_centrality(self.graph)
        self.ranked_degree = self.sort_dict(degree_rank)
        closeness_rank = nx.closeness_centrality(self.graph)
        self.ranked_closeness = self.sort_dict(closeness_rank)
        betweenness_rank = nx.betweenness_centrality(self.graph)
        self.ranked_betweenness = self.sort_dict(betweenness_rank)
        eigenvector_rank = nx.eigenvector_centrality(self.graph)
        self.ranked_eigenvector = self.sort_dict(eigenvector_rank)
        print("degree:\n")
        self.dict_print(self.ranked_degree)
        print("closeness:\n")
        self.dict_print(self.ranked_closeness)
        print("betweenness:\n")
        self.dict_print(self.ranked_betweenness)
        print("eigenvector:\n")
        self.dict_print(self.ranked_eigenvector)

    def sort_dict(self,dic):
        '''
        sorted dictionary desc
        '''
        ranked_dic = dict(sorted(dic.items(),key=lambda item: item[1],reverse=True))
        return ranked_dic
    def dict_print(self,dic):
        for k,v in dic.items():
            print(k,v)

if __name__ == "__main__":
    nextworker = nextworker(data_path)
    nextworker.data_loader()
    nextworker.build_graph()
    nextworker.get_graph_details()
    nextworker.get_rank_of_nodes()
    nextworker.visualize_network()