import networkx as nx
import pandas as pd
from modules.visibility_graph import visibility_graph  

def Chordal(rutas, int_max_clique, frec):
    names=str.split(rutas[0],"/")
    t=len(names)
    nombre= names[t-1]
    names = str.split(rutas[0],nombre)
    
    is_chordal = []
    for i in range(len(rutas)):
        P = visibility_graph(rutas[i], frec)
        is_chordal.append(nx.is_chordal(P))
    is_chordal            = pd.DataFrame(is_chordal)
    is_chordal.to_csv(names[0]+"is_chordal(visibility_graph).txt", sep = '\t',header = None,index = False)
    
    if(int_max_clique==1):
        p_is_chordal = []
        for i in range(len(rutas)):
            P = visibility_graph(rutas[i],frec)
            p = nx.make_max_clique_graph(P)
            p_is_chordal.append(nx.is_chordal(p))
        p_is_chordal = pd.DataFrame(p_is_chordal)
        p_is_chordal.to_csv(names[0]+"is_chordal(maxclique_graph).txt", sep = '\t',header = None,index = False)