import networkx as nx
import pandas as pd
from modules.visibility_graph import visibility_graph 
from modules.Functions import grado_max 

def Grade_Max(rutas, int_max_clique, frec):
    names=str.split(rutas[0],"/")
    t=len(names)
    nombre= names[t-1]
    names = str.split(rutas[0],nombre)
    grad_max = []
    for i in range(len(rutas)):
        P = visibility_graph(rutas[i],frec)
        grad_max.append(grado_max(P))
    
    grad_max = pd.DataFrame(grad_max)
    grad_max.to_csv(names[0]+"max_dregree(visibility_graph).txt", sep = '\t',header = None,index = False)
           
        
    if(int_max_clique==1):
        p_grad_max = []
        for i in range(len(rutas)):
            P = visibility_graph(rutas[i],frec)
            p = nx.make_max_clique_graph(P)
            p_grad_max.append(grado_max(p))
                
        p_grad_max = pd.DataFrame(p_grad_max)
        p_grad_max.to_csv(names[0]+"max_degree(maxclique_graph).txt", sep = '\t',header = None,index = False)