from networkx import (graph_clique_number, graph_number_of_cliques, find_cliques )
from pandas import DataFrame
from pathlib import Path   

def Cliques(P, tipo, ruta):
    RUTA =  ruta + '/NetWX/files/'
    path = Path(RUTA)
    path.mkdir(parents = True,exist_ok = True)
    
    graph_clique_num        = []
    graph_number_of_cliqs   = []
    graph_find_cliques      = []
    for i in range(len(P)):
        graph_clique_num.append(graph_clique_number(P[i]))
        graph_number_of_cliqs.append(graph_number_of_cliques(P[i]))
        graph_find_cliques.append(find_cliques(P[i]))
    graph_clique_num      = DataFrame(graph_clique_num)
    graph_number_of_cliqs = DataFrame(graph_number_of_cliqs)
    graph_find_cliques    = DataFrame(graph_find_cliques)
    graph_clique_num.to_csv(RUTA + tipo + " clique_num.txt", sep = '\t',header = None,index = False)
    graph_number_of_cliqs.to_csv(RUTA + tipo + " graph_number_of_cliqs.txt", sep = '\t',header = None,index = False)
    graph_find_cliques.to_csv(RUTA + tipo + " find_cliques.txt", sep = '\t',header = None,index = False)
    
