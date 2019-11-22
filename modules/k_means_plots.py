# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:41:23 2019

@author: ulipa
"""
from numpy import column_stack
from modules.kmeans_algoritm import kmeans
import matplotlib.pyplot as plt
def kmeans_plots(x, y, k, ruta, x_label, y_label, title): 
    data = column_stack((x,y))
    classifications, centers = kmeans(data, k)
    tipos = list(set(classifications))
    index_clas = []
    for j in tipos:
        data = []
        for i in range(len(classifications)):
            if(classifications[i] == j):
                data.append(i)
        index_clas.append(data)
    colors = ['b*', 'r*', 'g*', 'c*', 'm*', 'y*', 'k*', 'w*']
    plt.figure()
    plt.figtext(.5,.9, title, fontsize=18, ha='center')
    plt.xlabel(x_label, fontsize=14)
    plt.ylabel(y_label, fontsize=14)
    plt.grid(True)
    for j in range(len(index_clas)): 
        for i in range(len(y)):
            if(i in index_clas[j]):
                plt.plot(x[i], y[i], colors[j], marker = '$'+str(i+1)+'$', markersize= 9)
    plt.savefig(ruta + ' K-means ' + x_label + ' vs ' + y_label + '.png',dpi=300, transparent = True)
    plt.close()
