import networkx as nx
import matplotlib.pyplot as plt


def Plot(P,ruta,style,label):
    names=str.split(ruta,"/")
    t=len(names)
    nombre= names[t-1]
    names = str.split(ruta,nombre)
    nam   = str.split(nombre,'.')
    
    A = plt.figure()
    if(style==0): 
        nx.draw(P,with_labels=True)
    elif(style==1): 
        nx.draw(P, pos=nx.circular_layout(P), node_color='r', edge_color='b',with_labels=True)
    elif(style==2):
        nx.draw(P, pos = nx.kamada_kawai_layout(P))
    A.savefig(names[0]+nam[0]+label,dpi=300)
    A.clear()
