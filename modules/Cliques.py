import networkx as nx
import pandas as pd
from modules.visibility_graph import visibility_graph


def Cliques(rutas, int_max_clique,frec):
    names=str.split(rutas[0],"/")
    t=len(names)
    nombre= names[t-1]
    names = str.split(rutas[0],nombre)
    
    graph_clique_num        = []
    graph_number_of_cliqs   = []
    for i in range(len(rutas)):
        P = visibility_graph(rutas[i],frec)
        graph_clique_num.append(nx.graph_clique_number(P))
        graph_number_of_cliqs.append(nx.graph_number_of_cliques(P))
    graph_clique_num      = pd.DataFrame(graph_clique_num)
    graph_number_of_cliqs = pd.DataFrame(graph_number_of_cliqs)
    graph_clique_num.to_csv(names[0]+"_Graph_clique_num.txt", sep = '\t',header = None,index = False)
    graph_number_of_cliqs.to_csv(names[0]+"_Graph_number_of_cliqs.txt", sep = '\t',header = None,index = False)
    
    if(int_max_clique==1):
        p_graph_clique_num      = []
        p_graph_number_of_cliqs = []
        for i in range(len(rutas)):
            P = visibility_graph(rutas[i],frec)
            p = nx.make_max_clique_graph(P)
            p_graph_clique_num.append(nx.graph_clique_number(p))
            p_graph_number_of_cliqs.append(nx.graph_number_of_cliques(p))
        p_graph_clique_num      = pd.DataFrame(p_graph_clique_num)
        p_graph_number_of_cliqs = pd.DataFrame(p_graph_number_of_cliqs)
        p_graph_clique_num.to_csv(names[0] + "_p_Graph_graph_clique_num.txt", sep = '\t',header = None,index = False)
        p_graph_number_of_cliqs.to_csv(names[0] + "_p_Clique Graph_graph_number_of_cliqs.txt", sep = '\t',header = None,index = False)
                