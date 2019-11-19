from pandas import DataFrame
from modules.Functions import grado_max 
from pathlib import Path

def Grade_Max(P, tipo, ruta):
    RUTA =  ruta + '/NetWX/files/'
    path = Path(RUTA)
    path.mkdir(parents = True,exist_ok = True)
    
    grad_max = []
    for i in range(len(P)):
        grad_max.append(grado_max(P[i]))
        
    grad_max = DataFrame(grad_max)
    grad_max.to_csv(RUTA + tipo + " - max degree.txt", sep = '\t',header = None, index = False)
           
        