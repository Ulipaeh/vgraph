# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 11:39:57 2019

@author: ulipa
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:24:20 2019

@author: Ulises
"""
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication , QFormLayout,
                             QComboBox,QLineEdit,QTableView , QSplitter, QVBoxLayout, QMainWindow,QFileDialog, QLabel, QTableWidget)
from PyQt5.QtCore import Qt, QAbstractTableModel

from PyQt5.QtGui import QIcon
#from modules.Dialog import Dialog
# xls xlsx
import pyqtgraph as pg  
import scipy.io
from numpy import asarray
import pandas as pd
import sys

class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None


class Export(QMainWindow):

    def __init__(self):
        super(Export, self).__init__()
        self.initUI()

#%%
    def cargarSenial(self):
        self.archivo = QFileDialog.getOpenFileName(None, 'Open file', '/home')
        ruta = self.archivo[0]
        if(len(self.archivo[0])!=0):
            elementos = str.split(ruta,'/')
            nombre = elementos[-1]
            elementos = str.split(nombre,'.')
            self.extension = elementos[-1]
            if(self.extension == 'mat'):
                self.data = scipy.io.loadmat(ruta)
                keys = list(self.data.keys())
                for i in range(len(keys)):
                    if(type(keys[i])!= float):
                        self.dato_list.addItem(keys[i])
            elif(self.extension == 'xls' or self.extension =='xlsx'):
                self.data = pd.ExcelFile(ruta)
                sheets = self.data.sheet_names
                self.dato_list.addItems(sheets)
#%%
    def changedata(self):
        if(self.dato_list.currentIndex()!=0):
            if(self.extension == 'xls' or self.extension == 'xlsx'):
                data = self.data.parse(self.dato_list.currentText())
                model = pandasModel(data)
                self.tabla.setModel(model)
                self.len_txt.setText(str(len(data.index)))
                self.files_txt.setText(str(len(data.columns)))
            elif(self.extension == 'mat'):
                data = pd.DataFrame(self.data[self.dato_list.currentText()])
                model = pandasModel(data)
                self.tabla.setModel(model)
                self.len_txt.setText(str(len(data.index)))
                self.files_txt.setText(str(len(data.columns)))

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
        self.y=[]
        self.data = 0
        #################################################################
        ##     Definición de elementos contenedores
        #################################################################
        botones  = QVBoxLayout()
        results  = QFormLayout()
        tablalayout = QVBoxLayout()

        #################################################################
        ##     Elementos del layout botones
        ################################################################# 
        btnLoadSig = QPushButton('Load file')
        btnLoadSig.clicked.connect(self.cargarSenial)
        btnLoadSig.setStyleSheet("font-size: 18px")

        dato_lbl = QLabel('Variable: ')
        dato_lbl.setStyleSheet('font-size: 18px')
        self.dato_list = QComboBox()
        self.dato_list.currentIndexChanged.connect(self.changedata)
        
        files_lbl = QLabel('Files: ')
        files_lbl.setStyleSheet('font-size: 18px')
        self.files_txt = QLabel()
        self.files_txt.setStyleSheet('font-size: 18px')
        
        len_lbl = QLabel('length: ')
        len_lbl.setStyleSheet('font-size: 18px')
        self.len_txt = QLabel()
        self.len_txt.setStyleSheet('font-size: 18px')
        
        btn_start = QPushButton('Convert to .txt')
        btn_start.clicked.connect(self.cargarSenial)
        btn_start.setStyleSheet("font-size: 18px")

        
        #################################################################
        ##     Elementos de la Tabla
        ################################################################# 
        self.tabla = QTableView()
        tablalayout.addWidget(self.tabla)

        #################################################################
        ##     Colocar elementos en layout botones
        #################################################################
        botones.addWidget(btnLoadSig)
        results.addRow(dato_lbl, self.dato_list)
        results.addRow(files_lbl, self.files_txt)
        results.addRow(len_lbl, self.len_txt)
        botones.addLayout(results)
        botones.addWidget(btn_start)
 
        #################################################################
        ##     Colocar elementos en la ventana
        #################################################################        
        bot = QWidget()
        bot.setLayout(botones)
        tab = QWidget()
        tab.setLayout(tablalayout)

        contain.addWidget(tab)
        contain.addWidget(bot)
        self.setCentralWidget(contain)
        
if __name__ == '__cutSignals__':
    app = QApplication(sys.argv)
    ex = Export()
    sys.exit(app.exec_())
