# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 09:58:59 2019

@author: ulipa
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:24:20 2019

@author: Ulises
"""
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication , QFormLayout,
                             QComboBox,QLineEdit, QSplitter, QVBoxLayout, QMainWindow,QFileDialog, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from modules.k_means_plots import kmeans_plots
import pyqtgraph as pg  
from numpy import asarray
import pandas as pd
import sys

class K_means(QMainWindow):

    def __init__(self):
        super(K_means, self).__init__()
        self.initUI()

#%%
    def cargarSenial(self):
        self.aux = False
        self.list1.clear()
        self.list2.clear()
        self.nombreSenial = QFileDialog.getOpenFileNames(None, 'Open file(s)', '/home')
        self.rutas = self.nombreSenial[0]
        
        names = str.split(self.rutas[0],"/")
        t=len(names)
        nombre = names[t-1]
        self.names = str.split(self.rutas[0],nombre)   
        
        for i in range(len(self.rutas)):
            names=str.split(self.rutas[i],"/")
            t=len(names)
            nombre = names[t-1]
            self.list1.addItem(nombre)
            self.list2.addItem(nombre)
        if(len(self.rutas)!=0):
            self.btnStart.setEnabled(True)
        self.aux = True
        
    def K(self):
        x = asarray(pd.read_csv(self.rutas[self.list1.currentIndex()]))
        y = asarray(pd.read_csv(self.rutas[self.list2.currentIndex()]))
        k = int(self.list5.currentText())
        ruta = self.names[0]
        x_label = self.list3.currentText()
        y_label = self.list4.currentText()
        title = self.list6.currentText()
        kmeans_plots(x, y, k, ruta, x_label, y_label, title)
        
#%% 
    def initUI(self):
        pg.setConfigOption('background', 'w')
        self.setWindowTitle('K-means')
        self.setWindowIcon(QIcon("Icons\kmeans.png"))
        self.resize(500, 500)
        contain = QSplitter(Qt.Horizontal)
        #################################################################
        ##     Definición de variables globales
        #################################################################
        self.ruta = None
        self.nombreSenial = ''
        self.y = []
        self.aux = 0
        #################################################################
        ##     Definición de elementos contenedores
        #################################################################
        botones   = QVBoxLayout()
        results   = QFormLayout()
        #################################################################
        ##     Elementos del layout botones
        #################################################################
        btnLoad_files = QPushButton('Load files')
        btnLoad_files.clicked.connect(self.cargarSenial)
        btnLoad_files.setStyleSheet("font-size: 18px")
                
        x_file = QLabel('x-Axis')
        x_file.setStyleSheet('font-size: 18px')
        self.list1 = QComboBox()
        
        y_file = QLabel('y-Axis')
        y_file.setStyleSheet('font-size: 18px')
        self.list2 = QComboBox()
                
        x_lbl = QLabel('x-Label')
        x_lbl.setStyleSheet('font-size: 18px')
        
        y_lbl = QLabel('y-Label')
        y_lbl.setStyleSheet('font-size: 18px')
        
        self.list3 = QComboBox()
        items_lbl = ['Δ(G)','Δ(K(G))','ω(G)','ω(K(G))','G','K(G)']
        self.list3.addItems(items_lbl)
        self.list4 = QComboBox()
        self.list4.addItems(items_lbl)
        
        k_lbl = QLabel('Clusters (k): ')
        k_lbl.setStyleSheet('font-size: 18px')
        k_values = ['2','3','4','5','6']
        self.list5 = QComboBox()
        self.list5.addItems(k_values)
        
        title_lbl = QLabel('Iterations (max): ')
        title_lbl.setStyleSheet('font-size: 18px')
        title = ['Visibility graph G ','Maxclique graph K(G)']
        self.list6 = QComboBox()
        self.list6.addItems(title)
        
        self.btnStart = QPushButton('K-Means')
        self.btnStart.clicked.connect(self.K)
        self.btnStart.setStyleSheet("font-size: 18px")
        self.btnStart.setEnabled(False)
        
        #################################################################
        ##     Colocar elementos en layout botones
        #################################################################
        results.addRow(btnLoad_files)
        results.addRow(x_file,self.list1)
        results.addRow(y_file,self.list2)
        results.addRow(x_lbl,self.list3)
        results.addRow(y_lbl,self.list4)
        results.addRow(k_lbl,self.list5)
        results.addRow(title_lbl,self.list6)
        results.addRow(self.btnStart)
        botones.addLayout(results)     
        
        #################################################################
        ##     Colocar elementos en la ventana
        #################################################################        
        bot = QWidget()
        bot.setLayout(botones)

        contain.addWidget(bot)
        self.setCentralWidget(contain)
        
if __name__ == '__K_means__':
    app = QApplication(sys.argv)
    ex = K_means()
    sys.exit(app.exec_())
