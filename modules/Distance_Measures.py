from networkx import (center, diameter, extrema_bounding, periphery, radius)
from pandas import DataFrame
from pathlib import Path          

def Distance_measures(P, tipo, ruta):
    RUTA =  ruta + '/NetWX/files/'
    path = Path(RUTA)
    path.mkdir(parents = True,exist_ok = True)
    
    P_center            = []
    P_diameter          = []
    P_extrema_bounding  = []
    P_periphery         = []
    P_radius            = []
    for i in range(len(P)):
        P_center.append(center(P[i]))
        P_diameter.append(diameter(P[i]))
        P_extrema_bounding.append(extrema_bounding(P[i]))
        P_periphery.append(periphery(P[i]))
        P_radius.append(radius(P[i]))
    P_center           = DataFrame(P_center)
    P_diameter         = DataFrame(P_diameter)
    P_extrema_bounding = DataFrame(P_extrema_bounding)
    P_periphery        = DataFrame(P_periphery)
    P_radius           = DataFrame(P_radius)
    P_center.to_csv(RUTA + tipo + " - center.txt", sep = '\t',header = None,index = False)
    P_diameter.to_csv(RUTA + tipo +" - diameter.txt", sep = '\t',header = None,index = False)
    P_extrema_bounding.to_csv(RUTA + tipo +" - extrema_bounding.txt", sep = '\t',header = None,index = False)
    P_periphery.to_csv(RUTA + tipo + " - periphery.txt", sep = '\t',header = None,index = False)
    P_radius.to_csv(RUTA + tipo + " - radius.txt", sep = '\t',header = None,index = False)
                
            