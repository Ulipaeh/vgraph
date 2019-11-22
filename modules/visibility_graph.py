import numpy as np
import pandas as pd
from networkx import Graph
import matplotlib.pyplot as plt
from pathlib import Path

def is_visible (y ,a ,b ):
    isit = True
    c = a +1
    while isit and c < b:
        isit = y[c]<y[b]+(y[a]-y[b])*((b-c)/float(b -a ))
        c = c +1
    return isit

def visibility_graph(ruta,frec):
    names = str.split(ruta,"/")
    t = len(names)
    nombre = names[t-1]
    data = np.asarray(pd.read_csv(ruta,sep='\t', header=None))
#    if(min(data)[0]<=0):
#        funcion = np.vectorize(lambda x: x + (-1)*min(data)[0])
#        y = funcion(data)    
#    else:
#        y = data
    
    names = str.split(ruta,nombre)
    nam   = str.split(nombre,'.')
  
    RUTA =  names[0] + '/NetWX/images/'
    path = Path(RUTA)
    path.mkdir(parents = True,exist_ok = True)

    y = data
    
    plt.figure()
    plt.grid(True)
    plt.plot(y)
    plt.savefig(RUTA + nam[0]+'.png',dpi=300)
    plt.close()
    
        
    if(frec==0):
        m = 1
    elif(frec==1):
        m = 10
    elif(frec==2):
        m = 14
    elif(frec==3):
        m = 20
    elif(frec==4):
        m = 25
    elif(frec==5):
        m = 33
    elif(frec==6):
        m = 100
        
    data = []
    for j in range(0,len(y),m):
        data.append(y[j])
    y = data
    vals = []
    for j in range(int(len(y))):
        vals.append(float(y[j]))
    
    
    plt.figure()
    plt.grid(True)
    plt.bar(range (len( vals )),vals ,width =0.2 ,align ="center")
    plt.savefig(RUTA + nam[0]+'_bar_graph.png',dpi=300)
    plt.close()

    eds = []
    for a in range(len(vals)):
        for b in range(a+1,len(vals)):
            if is_visible(vals,a,b):
                eds.append((a,b))
    P = Graph(eds)
    return(P)
                
           