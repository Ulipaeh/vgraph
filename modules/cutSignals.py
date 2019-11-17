# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:24:20 2019

@author: Ulises
"""
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication , QFormLayout,
                             QComboBox,QLineEdit, QSplitter, QVBoxLayout, QMainWindow,QFileDialog, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QIntValidator
from modules.Dialog import Dialog

import pyqtgraph as pg  
from numpy import asarray, transpose, arange, where
import pandas as pd
import sys

class CutSignals(QMainWindow):

    def __init__(self):
        super(CutSignals, self).__init__()
        self.initUI()

#%%
    def cargarSenial(self):
        self.txt_total.setText('')
        self.lbl_inicio.setText('')
        self.lbl_final.setText('')
        self.seg_pos.clear()
        self.btnIniciar.setEnabled(True)
        self.plot1.clear()
        self.nombreSenial= QFileDialog.getOpenFileName(None, 'Open file', '/home')
        if(len(self.nombreSenial[0])!=0):
            print(self.nombreSenial)
            datos = pd.read_csv(self.nombreSenial[0],sep='\t', header=None)
            lineas= datos.shape[1]
            if(lineas == 1):
                self.y = asarray(datos[0])
                self.y_auto = datos[0]
            elif(lineas == 2):
                self.y = asarray(datos[1])
                self.y_auto = datos[1]
            self.plot1.setLabel('bottom',color='k', **{'font-size':'14pt'})
            self.plot1.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
            # Y1 axis   
            self.plot1.setLabel('left',color='k', **{'font-size':'14pt'})
            self.plot1.getAxis('left').setPen(pg.mkPen(color='k', width=1))
            names=str.split(self.nombreSenial[0],"/")
            t=len(names)
            self.nombre= names[t-1]
            self.plot1.setTitle(self.nombre)
            self.plot1.plot(self.y,pen='k')
            self.btnauto.setEnabled(True)
            
            
#%%
    def localizacion(self):
        if(self.aux == True):
            i = self.seg_pos.currentIndex()
            if(i == 0):
                self.lbl_inicio.setText('ini')
                self.lbl_final.setText('end')
            else:
                self.lbl_inicio.setText(str(self.inicio[i-1]))
                self.lbl_final.setText(str(self.final[i-1]))
#%%
    def colocar(self):
        inicio = int(self.lbl_inicio.text())
        final  = int(self.lbl_final.text())
        if(self.aux2 == True):
            self.lr.setRegion([inicio,final])

#%% 
    def autoseg(self):
        self.aux == False
        self.inicio = []
        self.final  = []
        self.seg_pos.clear()
        self.seg_pos.addItem('')
        if(len(self.txt_umbral.text())!=0 and len(self.txt_basal.text())!=0 and len(self.txt_ancho.text())!=0 
           and len(self.txt_separacion.text())!=0):
            umbral     = float(self.txt_umbral.text())
            basal      = float(self.txt_basal.text())
            ancho      = float(self.txt_ancho.text())
            separacion = float(self.txt_separacion.text())        
            y = self.y_auto
            
            loc_x = []
            for i in range(len(y)):
                if(y[i]>umbral):
                    loc_x.append(i) 
            loc = []
            for i in range(len(loc_x)):
                if(i<len(loc_x)-1):
                    if(loc_x[i+1]-loc_x[i]>ancho):
                        loc.append(loc_x[i])
            ini = []
            end = []        
            for i in range(len(loc)):
                x_ini   = arange(loc[i]-separacion,loc[i])
                y_ini   = y[x_ini]
                
                x_end   = arange(loc[i],loc[i] + separacion)
                y_end   = y[x_end]
                
                donde_ini = where(y_ini <= min(y_ini) + basal)[0]
                donde_fin = where(y_end <= min (y_ini) + basal)[0]
                
                if(len(donde_fin)!=0 ):
                    ini.append(x_ini[max(donde_ini)])
                    end.append(x_end[min(donde_fin)]) 
                         
            names = str.split(self.nombreSenial[0],self.nombre)
            nam   = str.split(self.nombre,'.') 
    
            for i in range(len(loc)):
                self.seg_pos.addItem(str(i+1))
                self.inicio.append(int(ini[i]))
                self.final.append(int(end[i]))
                data = pd.DataFrame(y[int(ini[i]):int(end[i])])
                data.to_csv(names[0]+nam[0]+'_seg_'+ str(i+1) +'.txt',sep ='\t', header = None, index = False)
            self.aux = True
            self.txt_total.setText(str(len(self.inicio)))
            self.btn_loc.setEnabled(True)
            self.btnauto.setEnabled(False)
        else:
            self.dialogo_error = Dialog('Error: Missing value ','Icons\error.png')
            self.dialogo_error.show()
            
#%%
    def enabledButtons(self):
        self.btnAdd.setEnabled(True)
        self.txtns.setEnabled(True)
        self.plot1.addItem(self.lr)
        self.btnIniciar.setEnabled(False)
        self.aux2 = True
        
        
#%%      
    def addInterval(self):
        if(len(self.txtns.text())==0):
            self.dialogo_error = Dialog('A segment number must be type() = int ','Icons\error.png')
            self.dialogo_error.show()
        else:
            self.contador  = int(self.txtns.text())
            regionSelected = self.lr.getRegion()
            ini = int(regionSelected[0])
            fin = int(regionSelected[1])
            self.duracion.append(self.y[ini:fin])
            self.duracion = transpose(self.duracion)
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
    def initUI(self):
        pg.setConfigOption('background', 'w')
        self.setWindowTitle('Cut Signal')
        self.setWindowIcon(QIcon("Icons\cut.png"))
        self.resize(1225, 700)
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
        self.aux = 0
        self.aux2 = False
        #################################################################
        ##     Definición de elementos contenedores
        #################################################################
        graficos = QVBoxLayout()
        botones  = QVBoxLayout()
        results2 = QFormLayout()
        results3 = QFormLayout()
        results  = QFormLayout()
        #################################################################
        ##     Elementos del layout botones
        #################################################################
        #Region for segment in signal
        self.lr = pg.LinearRegionItem([0,6000])
        
        btnLoadSig = QPushButton('Load signal')
        btnLoadSig.clicked.connect(self.cargarSenial)
        btnLoadSig.setStyleSheet("font-size: 18px")
        
        self.btnIniciar = QPushButton('Start segmentation')
        self.btnIniciar.clicked.connect(self.enabledButtons)
        self.btnIniciar.setEnabled(False)
        self.btnIniciar.setStyleSheet("font-size: 18px")

        self.btnAdd = QPushButton('Add segment')
        self.btnAdd.clicked.connect(self.addInterval)
        self.btnAdd.setEnabled(False)
        self.btnAdd.setStyleSheet("font-size: 18px")
        
        txtnumseg  = QLabel("Segment num:")
        txtnumseg.setStyleSheet("font-size: 18px")
                
        validator = QIntValidator()
        validator.setRange(100,999)  
        
        self.txtns = QLineEdit()
        self.txtns.setValidator(validator)
        self.txtns.setEnabled(False)
        
        lbl_umbral = QLabel('Amplitude aprox:')
        lbl_umbral.setStyleSheet("font-size: 18px")
        self.txt_umbral = QLineEdit()
        
        lbl_basal = QLabel('Baseline aprox:')
        lbl_basal.setStyleSheet("font-size: 18px")
        self.txt_basal = QLineEdit()
        
        lbl_ancho = QLabel('Length aprox:')
        lbl_ancho.setStyleSheet("font-size: 18px")
        self.txt_ancho = QLineEdit()
        
        lbl_separacion = QLabel('Distance:')
        lbl_separacion.setStyleSheet("font-size: 18px")
        self.txt_separacion = QLineEdit()
        
        self.btnauto = QPushButton('Start auto-segmentation')
        self.btnauto.clicked.connect(self.autoseg)
        self.btnauto.setStyleSheet("font-size: 18px")
        self.btnauto.setEnabled(False)
        
        lbl_total = QLabel('# of spikes:')
        lbl_total.setStyleSheet('font-size: 18px')
        
        self.txt_total = QLabel()
        self.txt_total.setStyleSheet('font-size: 18px')
        
        lbl_file = QLabel('Spike:')
        lbl_file.setStyleSheet("font-size: 18px")
        self.seg_pos = QComboBox()
        self.seg_pos.currentIndexChanged.connect(self.localizacion)
        
        self.lbl_inicio = QLabel()
        self.lbl_inicio.setStyleSheet("font-size: 18px")
        self.lbl_final = QLabel()
        self.lbl_final.setStyleSheet("font-size: 18px")
        
        self.btn_loc = QPushButton('Loc')
        self.btn_loc.setStyleSheet("font-size: 18px")
        self.btn_loc.clicked.connect(self.colocar)
        self.btn_loc.setEnabled(False)
        
#        self.seg_pos.currentIndexChanged.connect(self.plots)
        
        #################################################################
        ##     Elementos del layout graficos
        #################################################################
        self.plot1=pg.PlotWidget()
        self.plot1.setLabel('bottom',color='k', **{'font-size':'16pt'})
        self.plot1.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
        self.plot1.setLabel('left',color='k', **{'font-size':'16pt'})
        self.plot1.getAxis('left').setPen(pg.mkPen(color='k', width=1))
        self.plot1.showGrid(1,1,0.2)
        graficos.addWidget(self.plot1)
        #################################################################
        ##     Colocar elementos en layout botones
        #################################################################
        botones.addWidget(btnLoadSig)
        botones.addWidget(self.btnIniciar)
        results.addRow(txtnumseg, self.txtns)
        results.addRow(self.btnAdd)
        botones.addLayout(results)     
        
        results2.addRow(lbl_umbral, self.txt_umbral)
        results2.addRow(lbl_basal , self.txt_basal)
        results2.addRow(lbl_ancho , self.txt_ancho)
        results2.addRow(lbl_separacion, self.txt_separacion)
        botones.addLayout(results2)        
        botones.addWidget(self.btnauto)
        results3.addRow(lbl_total,self.txt_total)
        results3.addRow(lbl_file,self.seg_pos)
        results3.addRow(self.lbl_inicio,self.lbl_final)
        results3.addRow(self.btn_loc)
        botones.addLayout(results3)
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
