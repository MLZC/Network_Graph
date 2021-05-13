import numpy as np
import math
import networkx as nx
from subset import Subsets
from drawGraph import networker
import pandas as pd



class Shaply_calcer(object):

    def __init__(self,L,r,alpha,v_set,n): 
        '''
        L: the longest path of graph
        r: characteristic function jackson's approach
        alpha: the vector with size n*L, n =2^k - 1 , where is number of vertexes in the graph
        v_set: list of set
        n: the number of element in full set
        '''
        self.L = L
        self.r = r
        self.alpha = alpha
        self.v_set = v_set
        self.n = n
    def generate_vector(self):
        r_array = np.zeros((self.L,1))
        for i in range(self.L):
            r_array[i] = self.r**(i+1)
        self.r_array = r_array
        self.v_value = np.dot(self.alpha,self.r_array)
    def calc_Yi(self,k):
        sum = 0
        for i,j in enumerate(self.v_set):
            if k in j:
                continue
            else:
                t=set.copy(j)
                t.add(k)
                t_index = self.v_set.index(t)
                s_fac = math.factorial(len(j))
                n_fac = math.factorial(self.n)
                sum += (self.v_value[t_index]-self.v_value[i])*math.factorial(self.n-len(j)-1)*s_fac/n_fac
        return sum
    def start(self):
        Y_values = []
        self.generate_vector()
        for i in range(self.n):
            Y_values.append(self.calc_Yi(i))
        self.Y_values = Y_values
    def get_parameters(self):
        print("self.L : ",self.L)
        print("self.r : ",self.r)
        print("self.alpha :\n ",self.alpha)
        print("self.v_set :\n",self.v_set)
        print("self.n : ",self.n)
        print("self.r_array :\n",self.r_array)
        print("self.v_value :\n",self.v_value)
        print("self.Y_values :\n",self.Y_values)
if __name__ == "__main__":
    # ### Change your parameterss
    # L = 4
    # r = 1
    # n = 6
    # v_set = [{1,2,3,4,5,6},{1,2,3,4,5},{1,2,3,4,6},{1,2,3,5,6},{1,2,4,5,6},{1,3,4,5,6},{2,3,4,5,6},{3,4,5,6},{2,4,5,6},{2,3,5,6},{2,3,4,6},{2,3,4,5},{1,4,5,6},{1,3,5,6},{1,3,4,6},{1,3,4,5},{1,2,5,6},{1,2,4,6},{1,2,4,5},{1,2,3,6},{1,2,3,5},{1,2,3,4},{4,5,6},{3,5,6},{3,4,6},{3,4,5},{2,5,6},{2,4,6},{2,4,5},{2,3,6},{2,3,5},{2,3,4},{1,5,6},{1,4,6},{1,4,5},{1,3,6},{1,3,5},{1,3,4},{1,2,6},{1,2,5},{1,2,4},{1,2,3},{1,2},{1,3},{1,4},{1,5},{1,6},{2,3},{2,4},{2,5},{2,6},{3,4},{3,5},{3,6},{4,5},{4,6},{5,6}]

    # alpha = [(5,5,4,1),(4,4,2,0,),(3,2,1,0),(4,3,2,1),(4,4,2,0),(1,0,0,0),(3,2,1,0),(1,0,0,0),(3,2,1,0),(2,1,0,0),(1,0,0,0),(2,1,0,0,),(1,0,0,0),(2,0,0,0),(1,0,0,0),(1,0,0,0),(3,2,1,0),(2,1,0,0),(3,2,0,0),(2,1,0,0),(3,2,1,0),(3,2,1,0),(1,0,0,0),(1,0,0,0),(0,0,0,0),(0,0,0,0),(2,1,0,0),(1,0,0,0),(2,1,0,0),(0,0,0,0),(1,0,0,0),(1,0,0,0),(1,0,0,0),(0,0,0,0),(0,0,0,0),(1,0,0,0),(1,0,0,0),(1,0,0,0),(1,0,0,0),(2,1,0,0),(2,1,0,0),(2,1,0,0),(1,0,0,0),(1,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(1,0,0,0),(1,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(0,0,0,0),(1,0,0,0)]
    

    # ### Another example
    # # L=2
    # # r=1
    # # n=3
    # # v_set=[{1,2,3},{1,2},{1,3},{2,3},{1},{2},{3}]
    # # alpha=[(3,1),(1,0),(1,0),(1,0),(0,0),(0,0),(0,0)]

    # ### Do not change
    # alpha = np.array(alpha).reshape(-1,L)
    # Shaply = Shaply_calcer(L,r,alpha,v_set,n)
    # Shaply.start()
    # Shaply.get_parameters()


    ### 1000 nodes
    for i in range(100):

        data_path = './edges/edges_' + str(i) + '.csv'

        networker = networker(data_path)

        subsets_builder = Subsets(networker)
        print("***"*20)
        whole_set = nx.nodes(subsets_builder.networker.graph)

        L = len(whole_set)
        r = 1
        n = len(whole_set)

        v_set, alpha = subsets_builder.get_listOfAlphas(subsets_builder.edges,whole_set)
        ### Do not change
        alpha = np.array(alpha).reshape(-1,L)
        Shaply = Shaply_calcer(L,r,alpha,v_set,n)
        Shaply.start()
        Shaply.get_parameters()
        Y_values = Shaply.Y_values
        Y_valuesDF = pd.DataFrame(Y_values)
        Y_valuesDF.columns = ['Y']
        Y_valuesDF.to_csv('./results/results_' + data_path.split('_')[1],  index=None)
        # print(whole_set)
        # subsets = Subsets()
        # subsets_list = subsets.get_subsets(whole_set)
        # print(subsets_list)