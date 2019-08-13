# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:24:20 2019

@author: Ulises
"""
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication , QFormLayout, QLineEdit, QSplitter, QVBoxLayout, QMainWindow,QFileDialog, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QIntValidator
from modules.Dialog import Dialog

import pyqtgraph as pg  
import numpy as np
import pandas as pd
import sys

class CutSignals(QMainWindow):

    def __init__(self):
        super(CutSignals, self).__init__()
        self.initUI()

#%%
    def cargarSenial(self):
        self.btnIniciar.setEnabled(True)
        self.plot1.clear()
        self.nombreSenial= QFileDialog.getOpenFileName(None, 'Open file', '/home')
        if(len(self.nombreSenial[0])!=0):
            print(self.nombreSenial)
            datos = pd.read_csv(self.nombreSenial[0],sep='\t', header=None)
            lineas= datos.shape[1]
            if(lineas == 1):
                self.y = np.asarray(datos[0])
            elif(lineas == 2):
                self.y = np.asarray(datos[1])
            self.plot1.setLabel('bottom',color='k', **{'font-size':'12pt'})
            self.plot1.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
            # Y1 axis   
            self.plot1.setLabel('left',color='k', **{'font-size':'12pt'})
            self.plot1.getAxis('left').setPen(pg.mkPen(color='k', width=1))
            names=str.split(self.nombreSenial[0],"/")
            t=len(names)
            self.nombre= names[t-1]
            self.plot1.setTitle(self.nombre)
            self.plot1.plot(self.y,pen='k')

#%%
    def enabledButtons(self):
        self.btnAdd.setEnabled(True)
        self.txtns.setEnabled(True)
        self.plot1.addItem(self.lr)
        self.btnIniciar.setEnabled(False)
        
#%%      
    def addInterval(self):
        if(self.txtns.text()==None):
            self.dialogo_error = Dialog('A segment number must be entered','error.png')
            self.dialogo_error.show()
        else:
            self.contador  = int(self.txtns.text())
            regionSelected = self.lr.getRegion()
            ini = int(regionSelected[0])
            fin = int(regionSelected[1])
            self.duracion.append(self.y[ini:fin])
            self.duracion=np.transpose(self.duracion)
            df = pd.DataFrame(self.duracion)
            names = str.split(self.nombreSenial[0],self.nombre)
            nam   = str.split(self.nombre,'.')
            df.to_csv(names[0]+nam[0]+'_seg_'+str(self.contador)+'.txt',index=False,sep='\t', header = None, mode = 'w') 
            self.duracion = []        
            linea1= pg.InfiniteLine(pos= ini, angle=90, movable=False)
            linea2= pg.InfiniteLine(pos= fin, angle=90, movable=False)
            self.plot1.addItem(linea1)
            self.plot1.addItem(linea2)
            self.lr.setRegion([fin,fin+6000])


#%%
    def reboot(self):
        self.contador=0
        self.valorContador.setText("")

#%% 
    def initUI(self):
        pg.setConfigOption('background', 'w')
        self.setWindowTitle('Cut Signal')
        self.setWindowIcon(QIcon("cut.png"))
        self.resize(700, 400)
        contain=QSplitter(Qt.Horizontal)
        #################################################################
        ##     Definición de variables globales
        #################################################################
        self.ruta = None
        self.nombreSenial=''
        self.x=[]
        self.y=[]
        self.suspiros = []
        self.duracion = []
        self.intervalos = []
        self.contador=0
        self.ini = 0 
        self.fin = 0
        #################################################################
        ##     Definición de elementos contenedores
        #################################################################
        graficos = QVBoxLayout()
        botones = QVBoxLayout()
        results  = QFormLayout()
        #################################################################
        ##     Elementos del layout botones
        #################################################################
        #Region for segment in signal
        self.lr = pg.LinearRegionItem([0,6000])
        self.valorContador = QLabel('')
        
        btnLoadSig = QPushButton('Load signal')
        btnLoadSig.clicked.connect(self.cargarSenial)
        btnLoadSig.setStyleSheet("font-size: 12px")
        
        self.btnIniciar = QPushButton('Start segmentation')
        self.btnIniciar.clicked.connect(self.enabledButtons)
        self.btnIniciar.setEnabled(False)
        self.btnIniciar.setStyleSheet("font-size: 12px")

        self.btnAdd = QPushButton('Add segment')
        self.btnAdd.clicked.connect(self.addInterval)
        self.btnAdd.setEnabled(False)
        self.btnAdd.setStyleSheet("font-size: 12px")
        
        

        txtnumseg  = QLabel("Segment num:")
        txtnumseg.setStyleSheet("font-size: 12px")
        
        self.lbl_cursor  = QLabel()
        self.lbl_cursor.setStyleSheet("font-size: 12px")
        
        
        validator = QIntValidator(1, 100, self)        
        self.txtns = QLineEdit(self)
        self.txtns.setValidator(validator)
        self.txtns.setText('1')
        self.txtns.setEnabled(False)
        self.txtns.setStyleSheet("font-size: 12px")
        
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
        botones.addWidget(btnLoadSig)
        botones.addWidget(self.btnIniciar)
        botones.addWidget(self.btnAdd)
        results.addRow(txtnumseg, self.txtns)
        results.addRow(self.lbl_cursor)
        botones.addLayout(results)        
        #################################################################
        ##     Colocar elementos en layout graficos
        #################################################################

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
        
if __name__ == '__cutSignals__':
    app = QApplication(sys.argv)
    ex = CutSignals()
    sys.exit(app.exec_())
