from pandas import DataFrame
from modules.Functions import grado_max 
from pathlib import Path

def Degree(P, tipo, ruta):
    RUTA =  ruta + '/NetWX/files/'
    path = Path(RUTA)
    path.mkdir(parents = True,exist_ok = True)
    
    max_degree = []
    for i in range(len(P)):
        max_degree.append(grado_max(P[i]))
        
    max_degree = DataFrame(max_degree)
    max_degree.to_csv(RUTA + tipo + " - max degree.txt", sep = '\t',header = None, index = False)
           
        