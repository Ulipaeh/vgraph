import networkx as nx
import pandas as pd
from modules.visibility_graph import visibility_graph            

def Distance_measures(rutas, int_max_clique, frec):
    names=str.split(rutas[0],"/")
    t=len(names)
    nombre= names[t-1]
    names = str.split(rutas[0],nombre)
    
    center            = []
    diameter          = []
    extrema_bounding  = []
    periphery         = []
    radius            = []
    for i in range(len(rutas)):
        P = visibility_graph(rutas[i],frec)
        center.append(nx.center(P))
        diameter.append(nx.diameter (P))
        extrema_bounding.append(nx.extrema_bounding(P))
        periphery.append(nx.periphery(P))
        radius.append(nx.radius(P))
    center           = pd.DataFrame(center)
    diameter         = pd.DataFrame(diameter)
    extrema_bounding = pd.DataFrame(extrema_bounding)
    periphery        = pd.DataFrame(periphery)
    radius           = pd.DataFrame(radius)
    center.to_csv(names[0]+"center(visibility_graph).txt", sep = '\t',header = None,index = False)
    diameter.to_csv(names[0]+"diameter(visibility_graph).txt", sep = '\t',header = None,index = False)
    extrema_bounding.to_csv(names[0]+"extrema_bounding(visibility_graph).txt", sep = '\t',header = None,index = False)
    periphery.to_csv(names[0]+"periphery(visibility_graph).txt", sep = '\t',header = None,index = False)
    radius.to_csv(names[0]+"radius(visibility_graph).txt", sep = '\t',header = None,index = False)
                
    if(int_max_clique==1):
        p_center            = []
        p_diameter          = []
        p_extrema_bounding  = []
        p_periphery         = []
        p_radius            = []
        for i in range(len(rutas)):
            P = visibility_graph(rutas[i],frec)
            p = p = nx.make_max_clique_graph(P)
            p_center.append(nx.center(p))
            p_diameter.append(nx.diameter (p))
            p_extrema_bounding.append(nx.extrema_bounding(p))
            p_periphery.append(nx.periphery(p))
            p_radius.append(nx.radius(p))  
        p_center           = pd.DataFrame(p_center)
        p_diameter         = pd.DataFrame(p_diameter)
        p_extrema_bounding = pd.DataFrame(p_extrema_bounding)
        p_periphery        = pd.DataFrame(p_periphery)
        p_radius           = pd.DataFrame(p_radius)
        p_center.to_csv(names[0]+"center(maxclique_graph).txt", sep = '\t',header = None,index = False)
        p_diameter.to_csv(names[0]+"diameter(maxclique_graph).txt", sep = '\t',header = None,index = False)
        p_extrema_bounding.to_csv(names[0]+"extrema_bounding(maxclique_graph).txt", sep = '\t',header = None,index = False)
        p_periphery.to_csv(names[0]+"periphery(maxclique_graph).txt", sep = '\t',header = None,index = False)
        p_radius.to_csv(names[0]+"radius(maxclique_graph).txt", sep = '\t',header = None,index = False)
            