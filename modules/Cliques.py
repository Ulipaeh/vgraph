import networkx as nx
import pandas as pd
from modules.visibility_graph import visibility_graph
from pathlib import Path   

def Cliques(rutas, int_max_clique,frec):
    names=str.split(rutas[0],"/")
    t=len(names)
    nombre= names[t-1]
    names = str.split(rutas[0],nombre)
    
    RUTA =  names[0] + '/NetWX/files/'
    path = Path(RUTA)
    path.mkdir(parents = True,exist_ok = True)
    
    graph_clique_num        = []
    graph_number_of_cliqs   = []
    graph_find_cliques      = []
    for i in range(len(rutas)):
        P = visibility_graph(rutas[i],frec)
        graph_clique_num.append(nx.graph_clique_number(P))
        graph_number_of_cliqs.append(nx.graph_number_of_cliques(P))
        graph_find_cliques.append(nx.find_cliques(P))
    graph_clique_num      = pd.DataFrame(graph_clique_num)
    graph_number_of_cliqs = pd.DataFrame(graph_number_of_cliqs)
    graph_find_cliques    = pd.DataFrame(graph_find_cliques)
    graph_clique_num.to_csv(RUTA+"clique_num(visibility_graph).txt", sep = '\t',header = None,index = False)
    graph_number_of_cliqs.to_csv(RUTA+"graph_number_of_cliqs(visibility_graph).txt", sep = '\t',header = None,index = False)
    graph_find_cliques.to_csv(RUTA+"find_cliques(visibility_graph).txt", sep = '\t',header = None,index = False)
    
    if(int_max_clique==1):
        p_graph_clique_num      = []
        p_graph_number_of_cliqs = []
        p_graph_find_cliques    = []
        for i in range(len(rutas)):
            P = visibility_graph(rutas[i],frec)
            p = nx.make_max_clique_graph(P)
            p_graph_clique_num.append(nx.graph_clique_number(p))
            p_graph_number_of_cliqs.append(nx.graph_number_of_cliques(p))
            p_graph_find_cliques.append(nx.find_cliques(p))
        p_graph_clique_num      = pd.DataFrame(p_graph_clique_num)
        p_graph_number_of_cliqs = pd.DataFrame(p_graph_number_of_cliqs)
        p_graph_find_cliques    = pd.DataFrame(p_graph_find_cliques)
        p_graph_number_of_cliqs.to_csv(RUTA+"graph_number_of_cliqs(maxclique_graph).txt", sep = '\t',header = None,index = False)
        p_graph_clique_num.to_csv(RUTA + "clique_num(maxclique_graph).txt", sep = '\t',header = None,index = False)
        p_graph_find_cliques.to_csv(RUTA+"find_cliques(maxclique_graph).txt", sep = '\t',header = None,index = False)
                