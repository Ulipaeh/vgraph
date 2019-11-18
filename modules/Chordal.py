from networkx import is_chordal
from pandas import DataFrame
from pathlib import Path   

def Chordal(P, tipo, ruta):
    RUTA =  ruta + '/NetWX/files/'
    path = Path(RUTA)
    path.mkdir(parents = True,exist_ok = True)
    
    P_is_chordal = []
    for i in range(len(P)):
        P_is_chordal.append(is_chordal(P[i]))
    P_is_chordal = DataFrame(is_chordal)
    P_is_chordal.to_csv(RUTA + tipo +" is_chordal.txt", sep = '\t',header = None,index = False)
    