from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QLabel, QToolBar, QAction, QApplication, QLineEdit, QCheckBox ,
                              QWidget, QComboBox, QSplitter, QDialog, QDialogButtonBox, QPushButton, QVBoxLayout, QStatusBar, QFormLayout, QMenuBar)
from PyQt5.QtCore import Qt
from modules.cutSignals import CutSignals
from modules.visibility_graph import visibility_graph
from modules.Plot import Plot
from modules.Cliques import Cliques
from modules.Distance_Measures import Distance_measures
from modules.Chordal import Chordal
from modules.Grade_Max import Grade_Max

import sys
import numpy as np 
import pandas as pd
import networkx as nx
import pyqtgraph as pg

class Dialog(QDialog):
    def __init__(self, label, icon):
        super().__init__()
        lay = QVBoxLayout(self)
        
        self.setWindowFlag(Qt.WindowContextHelpButtonHint,False)

        self.icon = icon
        self.setWindowIcon(QIcon(self.icon))
        
        self.setWindowTitle('Message')
        self.label = label

        lbl = QLabel(self.label)

        dialogbutton = QDialogButtonBox()
        dialogbutton.setOrientation(Qt.Horizontal)
        dialogbutton.setStandardButtons(QDialogButtonBox.Ok)

        lay.addWidget(lbl)
        lay.addWidget(dialogbutton)

        dialogbutton.accepted.connect(self.accept)
        dialogbutton.rejected.connect(self.reject)

class Principal(QMainWindow):
    def cutSignal_boton(self):
        self.cut_signal = CutSignals()
        self.cut_signal.show()
    def visibility_graph_button(self):
        names=str.split(self.rutas[0],"/")
        t=len(names)
        self.nombre= names[t-1]
        names = str.split(self.rutas[0],self.nombre)
        for i in range(len(self.rutas)):
            P = visibility_graph(self.rutas[i],self.list2.currentIndex())
            Plot(P,self.rutas[i],self.list1.currentIndex(),'_visibility_graph.png')
            if(self.int_max_clique==1):
                p = nx.make_max_clique_graph(P)
                Plot(p,self.rutas[i],self.list1.currentIndex(),'_max_clique_graph.png')
        if(self.int_1 == 1):
            Cliques(self.rutas, self.int_max_clique, self.list2.currentIndex())
         
        if(self.int_2 == 1):
            Distance_measures(self.rutas, self.int_max_clique, self.list2.currentIndex())
        
        if(self.int_3 == 1):
            Chordal(self.rutas, self.int_max_clique, self.list2.currentIndex())
        
        if(self.int_4 == 1):
            Grade_Max(self.rutas, self.int_max_clique, self.list2.currentIndex())
            
        self.dialogo_done = Dialog('Done!','done.png')
        self.dialogo_done.show()
        
        
#%%
    def cargarSenial(self):
        self.list3.clear()
        self.nombreSenial= QFileDialog.getOpenFileNames(None, 'Open file(s)', '/home')
        self.rutas = self.nombreSenial[0]
        
        self.dialog = Dialog(str(len(self.rutas))+' Files(s) loaded(s)','open.png')
        self.dialog.show()
        self.list3.addItem('')
        for i in range(len(self.rutas)):
            names=str.split(self.rutas[i],"/")
            t=len(names)
            nombre= names[t-1]
            self.list3.addItem(nombre)
        self.plot1.clear()
            
        if(len(self.rutas)==0):
            self.btn1.setEnabled(False)
            self.lbl_num_files.setStyleSheet("color : red; ")
            self.lbl_num_files.setText("Files loaded: "+str(len(self.rutas)))
        else:
            self.btn1.setEnabled(True)
            self.lbl_num_files.setStyleSheet("color : blue; ")
            self.lbl_num_files.setText("Files loaded: "+str(len(self.rutas)))
#%%
    def state_check_1(self):
        if(self.int_1 == 0):
            self.int_1 = 1
        elif(self.int_1 ==1):
            self.int_1 = 0         
    def state_check_2(self):
        if(self.int_2 == 0):
            self.int_2 = 1
        elif(self.int_2 ==1):
            self.int_2 = 0
    def state_check_3(self):
        if(self.int_3 == 0):
            self.int_3 = 1
        elif(self.int_3 ==1):
            self.int_3 = 0
    def state_check_4(self):
        if(self.int_4 == 0):
            self.int_4 = 1
        elif(self.int_4 ==1):
            self.int_4 = 0
    def state_check_max_clique(self, state):
        if(state == Qt.Checked): 
            self.int_max_clique = 1 
        else: 
            self.int_max_clique = 0
    def plots(self):
        self.plot1.clear()
        i= self.list3.currentIndex()-1
        
        data = pd.read_csv(self.rutas[i],sep='\t', header=None)
        lineas= data.shape[1]
        if(lineas == 1):
            self.y = np.asarray(data[0])
        elif(lineas == 2):
            self.y = np.asarray(data[1])
        self.plot1.setLabel('bottom',color='k', **{'font-size':'12pt'})
        self.plot1.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
        # Y1 axis   
        self.plot1.setLabel('left',color='k', **{'font-size':'12pt'})
        self.plot1.getAxis('left').setPen(pg.mkPen(color='k', width=1))
        names=str.split(self.rutas[i],"/")
        t=len(names)
        nombre= names[t-1]
        self.plot1.setTitle(nombre)
        self.plot1.plot(self.y,pen='k')
        
#%% 
    def __init__(self):
        super().__init__()
        pg.setConfigOption('background', 'w')
        self.setWindowTitle('NetWX')
        self.setWindowIcon(QIcon("icon.ico"))
        self.resize(700, 400)
        contain=QSplitter(Qt.Horizontal)
        #################################################################
        ##     Definición de variables globales
        #################################################################
        self.rutas = ''
        self.nombreSenial=''
        self.x=[]
        self.y=[]
        self.int_1    = 0
        self.int_2    = 0
        self.int_3    = 0
        self.int_4    = 0
        self.int_max_clique = 0
        #################################################################
        ##     Barra de Herramientas
        #################################################################
        self.barra_estado = QStatusBar()
        self.setStatusBar(self.barra_estado)
        
        barra_herr = QToolBar("Toolbar")
        self.addToolBar(barra_herr)
        
        barra_menu = QMenuBar()
        self.setMenuBar(barra_menu)
        
        menu_archivo = barra_menu.addMenu('&File')
        menu_algorithms = barra_menu.addMenu('&Algorithms')
  
        abrir_action = QAction(QIcon('open.png'), 'Open File(s)', self)
        abrir_action.setToolTip('Open File(s)')
        abrir_action.setStatusTip('Open File(s)')
        abrir_action.triggered.connect(self.cargarSenial)
        barra_herr.addAction(abrir_action)
        menu_archivo.addAction(abrir_action)
        
        cortar_action = QAction(QIcon('cut.png'), 'Cut Signal', self)
        cortar_action.setToolTip('Cut Signal')
        cortar_action.setStatusTip('Cut Signal')
        cortar_action.triggered.connect(self.cutSignal_boton)
        barra_herr.addAction(cortar_action)
        
        self.chordal_action = QAction('Chordal',self ,checkable=True)
        self.chordal_action.triggered.connect(self.state_check_3)
        self.chordal_action.setToolTip('Algorithms for chordal graphs.')
        self.chordal_action.setStatusTip('Algorithms for chordal graphs.')
        menu_algorithms.addAction(self.chordal_action)
        
        self.cliques_action = QAction('Clique',self ,checkable=True)
        self.cliques_action.triggered.connect(self.state_check_1)
        self.cliques_action.setToolTip('Functions for finding and manipulating cliques.')
        self.cliques_action.setStatusTip('Functions for finding and manipulating cliques.')
        menu_algorithms.addAction(self.cliques_action)
        
        self.distance_measures_action = QAction('Distance Measures',self ,checkable=True)
        self.distance_measures_action.triggered.connect(self.state_check_2)
        self.distance_measures_action.setToolTip('Graph diameter, radius, eccentricity and other properties')
        self.distance_measures_action.setStatusTip('Graph diameter, radius, eccentricity and other properties')
        menu_algorithms.addAction(self.distance_measures_action)
        
        self.grade_max_action = QAction('Maximum Dregree',self ,checkable=True)
        self.grade_max_action.triggered.connect(self.state_check_4)
        self.grade_max_action.setToolTip('Graph Maximum dregree')
        self.grade_max_action.setStatusTip('Graph Maximum dregree')
        menu_algorithms.addAction(self.grade_max_action)
        

        #################################################################
        ##     Definición de elementos contenedores
        #################################################################
        graficos = QVBoxLayout()
        botones = QVBoxLayout()
        results  = QFormLayout()
        #################################################################
        ##     Elementos del layout botones
        #################################################################
        lbl2 = QLabel("Sampling frequency:")
        lbl2.setStyleSheet("font-size: 12px")
        
        self.txt1 = QLineEdit("")
        self.txt1.setEnabled(True)
        self.txt1.setStyleSheet("font-size: 12px")
                
        lbl_lista1 = QLabel("Graph layout:")
        lbl_lista1.setStyleSheet("font-size: 12px")
        
        self.list1 = QComboBox()
        self.list1.addItem("None")
        self.list1.addItem("Circular layout")
        self.list1.addItem("Kamada kawai layout")
        
        self.list2 = QComboBox()
        self.list2.addItem("100%")
        self.list2.addItem("10%")
        self.list2.addItem("1%")
        
        self.list3 = QComboBox()
        self.list3.currentIndexChanged.connect(self.plots)
        
        lbl_check1 = QLabel("Make maxclique graph")
        lbl_check1.setStyleSheet("font-size: 12px")
        
        self.check1 = QCheckBox()
        self.check1.stateChanged.connect(self.state_check_max_clique) 
        
        self.lbl_num_files = QLabel("Files loaded: ")
        self.lbl_num_files.setStyleSheet("font-size: 12px")
        
        lbl_file = QLabel("File: ")
        lbl_file.setStyleSheet("font-size: 12px")
        
        self.btn1 = QPushButton('Visibility graph')
        self.btn1.clicked.connect(self.visibility_graph_button)
        self.btn1.setStyleSheet("font-size: 12px")
        self.btn1.setEnabled(False)
        #################################################################
        ##     Elementos del layout graficos
        #################################################################
        self.plot1=pg.PlotWidget()
        self.plot1.setLabel('bottom',color='k', **{'font-size':'12pt'})
        self.plot1.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
        self.plot1.setLabel('left',color='k', **{'font-size':'12pt'})
        self.plot1.getAxis('left').setPen(pg.mkPen(color='k', width=1))
        self.plot1.showGrid(1,1,0.2)
        graficos.addWidget(self.plot1)
        #################################################################
        ##     Colocar elementos en layout botones
        #################################################################
        
        results.addRow(self.lbl_num_files)
        results.addRow(lbl_file,self.list3)
        results.addRow(lbl2, self.list2)
        results.addRow(lbl_lista1,self.list1)
        results.addRow(lbl_check1,self.check1)
        botones.addLayout(results) 
        botones.addWidget(self.btn1)
        #################################################################
        ##     Colocar elementos en la ventana
        #################################################################
        bot = QWidget()
        bot.setLayout(botones)
        gra = QWidget()
        gra.setLayout(graficos)

        contain.addWidget(gra)
        contain.addWidget(bot)

        self.setCentralWidget(contain)
        self.show()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_())
        
        
        