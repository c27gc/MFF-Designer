from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import os
from engineering_notation import EngNumber
import decimal
import numpy as np

class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        styleFile=os.path.join(os.path.split(__file__)[0],"combo.css")
        styleSheetStr = open(styleFile,"r").read()
        styleFile2=os.path.join(os.path.split(__file__)[0],"line.css")
        styleSheetStr2 = open(styleFile2,"r").read()
        self.setWindowTitle('Filter Fitter Prototype')
        #self.setStyleSheet("color:white; background: #002833")
        self.grid = QtGui.QGridLayout()
        self.label0 = QtGui.QLabel("Filter Response Specification")
        self.label0.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label0,1,0,1,2)

        """self.label1 = QtGui.QLabel("Of Filter's")
        self.label1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label1,2,0,1,2)

        self.label2 = QtGui.QLabel("Frequency Response")
        self.label2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label2,3,0,1,2)"""

        self.label3 = QtGui.QLabel("fo")
        self.label3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label3,2,0,1,1)
        self.label3Edit = QtGui.QLineEdit()
        self.label3Edit.editingFinished.connect(self.validation)
        self.label3Edit.setStyleSheet(styleSheetStr2)
        #self.label3Edit.setFixedWidth(200)
        self.grid.addWidget(self.label3Edit,2,1,1,1)

        self.label4 = QtGui.QLabel("A")
        self.label4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label4,3,0,1,1)
        self.label4Edit = QtGui.QLineEdit()
        self.label4Edit.editingFinished.connect(self.validation)
        self.label4Edit.setStyleSheet(styleSheetStr2)
        #self.label4Edit.setFixedWidth(200)
        self.grid.addWidget(self.label4Edit,3,1,1,1)

        self.label5 = QtGui.QLabel("Q")
        self.label5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label5,4,0,1,1)
        self.label5Edit = QtGui.QLineEdit()
        self.label5Edit.editingFinished.connect(self.validation)
        self.label5Edit.setStyleSheet(styleSheetStr2)
        #self.label5Edit.setFixedWidth(200)
        self.grid.addWidget(self.label5Edit,4,1,1,1)

        self.label6 = QtGui.QLabel("Approximated Mobil Parameter")
        self.label6.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label6,5,0,1,2)

        self.label6 = QtGui.QLabel("C")
        self.label6.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label6,6,0,1,1)
        self.label6Edit = QtGui.QLineEdit()
        self.label6Edit.textChanged.connect(self.validation)
        self.label6Edit.textEdited.connect(self.valaux)
        self.label6Edit.setStyleSheet(styleSheetStr2)
        #self.label6Edit.setFixedWidth(200)
        self.grid.addWidget(self.label6Edit,6,1,1,1)

        self.boton = QtGui.QPushButton('HELP', self)
        self.boton.setStyleSheet("color:white; background: #173f5f")##173f5f
        #self.connect(self.boton, QtCore.SIGNAL('clicked()'),self.calcular)
        #boton.setMinimumWidth(100)
        self.grid.addWidget(self.boton,7,0,1,2)

        self.label6 = QtGui.QLabel("Parameter's Tolerance")
        self.label6.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label6,8,0,1,2)

        self.label7 = QtGui.QLabel("R1a tol")
        self.label7.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label7,9,0,1,1)
        self.label7Edit = QtGui.QComboBox()
        #self.label7Edit.setStyleSheet("QCombobox:!editable{border: 1px solid white; color: white;}")
        self.label7Edit.setStyleSheet(styleSheetStr)
        self.label7Edit.addItems(["E6 : 20%","E12 : 10%","E24 : 5%","E48 : 2%","E96 : 1%","E192 : 0.5%",])
        #self.label7Edit.setFixedWidth(200)
        self.grid.addWidget(self.label7Edit,9,1,1,1)

        self.label8 = QtGui.QLabel("R1b tol")
        self.label8.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label8,10,0,1,1)
        self.label8Edit = QtGui.QComboBox()
        self.label8Edit.setStyleSheet(styleSheetStr)
        self.label8Edit.addItems(["E6 : 20%","E12 : 10%","E24 : 5%","E48 : 2%","E96 : 1%","E192 : 0.5%",])
        #self.label8Edit.setFixedWidth(200)
        self.grid.addWidget(self.label8Edit,10,1,1,1)

        self.label9 = QtGui.QLabel("R2 tol")
        self.label9.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label9,11,0,1,1)
        self.label9Edit = QtGui.QComboBox()
        self.label9Edit.setStyleSheet(styleSheetStr)
        self.label9Edit.addItems(["E6 : 20%","E12 : 10%","E24 : 5%","E48 : 2%","E96 : 1%","E192 : 0.5%",])
        #self.label9Edit.setFixedWidth(200)
        self.grid.addWidget(self.label9Edit,11,1,1,1)

        """self.label92 = QtGui.QLabel("R3 tol")
        self.label92.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label92,11,0,1,1)
        self.label92Edit = QtGui.QComboBox()
        self.label92Edit.setStyleSheet(styleSheetStr)
        self.label92Edit.addItems(["E6 : 20%","E12 : 10%","E24 : 5%","E48 : 2%","E96 : 1%","E192 : 0.5%",])
        #self.label92Edit.setFixedWidth(200)
        self.grid.addWidget(self.label92Edit,11,1,1,1)"""

        self.label10 = QtGui.QLabel("C tol")
        self.label10.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label10,12,0,1,1)
        self.label10Edit = QtGui.QComboBox()
        self.label10Edit.currentIndexChanged.connect(self.validation)
        self.label10Edit.setStyleSheet(styleSheetStr)
        self.label10Edit.addItems(["E6 : 20%","E12 : 10%","E24 : 5%","E48 : 2%","E96 : 1%","E192 : 0.5%",])
        #self.label10Edit.setFixedWidth(200)
        self.grid.addWidget(self.label10Edit,12,1,1,1)

        self.label102 = QtGui.QLabel("n")
        self.label102.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label102,13,0,1,1)
        self.label102Edit = QtGui.QLineEdit()
        self.label102Edit.setReadOnly(True)
        self.label102Edit.setStyleSheet("background: lightgray")
        #self.label102Edit.setFixedWidth(200)
        self.grid.addWidget(self.label102Edit,13,1,1,1)

        self.labelb1 = QtGui.QLabel("Type of Filter")
        self.labelb1.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.labelb1,1,2,1,1)
        self.comboxb1 = QtGui.QComboBox()
        self.comboxb1.setStyleSheet(styleSheetStr)
        self.comboxb1.addItems(["band-pass","low-pass"])
        self.comboxb1.currentIndexChanged.connect(self.verification)
        #self.labelb1Edit.setFixedWidth(200)
        self.grid.addWidget(self.comboxb1,1,3,1,1)

        self.labelb2 = QtGui.QLabel("Topology")
        self.labelb2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.labelb2.setStyleSheet("border: 4px solid white; background-color:white;")
        #self.labelb2.setMinimumWidth(400)
        self.labelb2.setPixmap(QtGui.QPixmap(os.getcwd() + "/pb.png"))

        self.grid.addWidget(self.labelb2,2,2,5,2)

        self.boton = QtGui.QPushButton('CALCULATE', self)
        self.boton.setStyleSheet("color:white; background: #173f5f")##173f5f
        self.connect(self.boton, QtCore.SIGNAL('clicked()'),self.calcular)
        #boton.setMinimumWidth(100)
        self.grid.addWidget(self.boton,7,2,1,2)

        self.labelb3 = QtGui.QLabel("Fitted Parameters")
        self.labelb3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.labelb3,8,2,1,2)



        self.labelb5 = QtGui.QLabel("R1a")
        self.labelb5.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.labelb5,9,2,1,1)
        self.labelb5Edit = QtGui.QLineEdit()
        self.labelb5Edit.setStyleSheet(styleSheetStr2)
        #self.labelb5Edit.setFixedWidth(200)
        self.grid.addWidget(self.labelb5Edit,9,3,1,1)

        self.labelb6 = QtGui.QLabel("R1b")
        self.labelb6.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.labelb6,10,2,1,1)
        self.labelb6Edit = QtGui.QLineEdit()
        self.labelb6Edit.setStyleSheet(styleSheetStr2)
        #self.labelb6Edit.setFixedWidth(200)
        self.grid.addWidget(self.labelb6Edit,10,3,1,1)

        self.labelb7 = QtGui.QLabel("R2")
        self.labelb7.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.labelb7,11,2,1,1)
        self.labelb7Edit = QtGui.QLineEdit()
        self.labelb7Edit.setStyleSheet(styleSheetStr2)
        #self.labelb7Edit.setFixedWidth(200)
        self.grid.addWidget(self.labelb7Edit,11,3,1,1)

        self.labelb4 = QtGui.QLabel("C")
        self.labelb4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.labelb4,12,2,1,1)
        self.labelb4Edit = QtGui.QLineEdit()
        self.labelb4Edit.setStyleSheet(styleSheetStr2)
        #self.labelb4Edit.setFixedWidth(200)
        self.grid.addWidget(self.labelb4Edit,12,3,1,1)

        self.labelb8 = QtGui.QLabel("MSE")
        self.labelb8.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.labelb8,13,2,1,1)
        self.labelb8Edit = QtGui.QLineEdit()
        self.labelb8Edit.setStyleSheet(styleSheetStr2)
        #self.labelb8Edit.setFixedWidth(200)
        self.grid.addWidget(self.labelb8Edit,13,3,1,1)

        self.labelbd = QtGui.QLabel("DIAGRAMA DE BODE")
        self.labelbd.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.labelbd.setStyleSheet("border: 4px solid white; background: #173f5f; color:white ")
        self.labelbd.setText("Status")
        self.grid.addWidget(self.labelbd,14,0,1,4)
        #self.labelbd.setFixedWidth(800)
        self.labelbd.setFixedHeight(200)

        #self.setFixedWidth(800)
        #self.setMinimumWidth(800)
        self.setMinimumWidth(1000)
        self.setLayout(self.grid)
        self.showMaximized()
        self.count = True
        self.validat = False
        self.varAux = False

    def valaux(self):
        self.count = True
        print("paso")

    def calcular(self):
        dic1 = {0:20, 1:10, 2:5, 3:2, 4:1, 5:0.5}
        if self.validat:
            if self.comboxb1.currentIndex() == 0:
                Ctol = dic1[self.label10Edit.currentIndex()]
                R1atol = dic1[self.label7Edit.currentIndex()]
                R1btol = dic1[self.label8Edit.currentIndex()]
                R2tol = dic1[self.label9Edit.currentIndex()]

                C,R1a,R1b,R2 = self.pBand(self.fn,self.Qn,self.An,self.Cn,Ctol,R1atol,R1btol,R2tol)
                self.labelb5Edit.setText(str(R1a))
                self.labelb6Edit.setText(str(R1b))
                self.labelb7Edit.setText(str(R2))
                self.labelb4Edit.setText(str(C))
            if self.comboxb1.currentIndex() == 1:
                Ctol = dic1[self.label10Edit.currentIndex()]
                R1tol = dic1[self.label7Edit.currentIndex()]
                R2tol = dic1[self.label8Edit.currentIndex()]
                R3tol = dic1[self.label9Edit.currentIndex()]

                R1,R2,R3,C = self.pLow(self.fn,self.Qn,self.An,self.Cn,Ctol,R1tol,R2tol,R3tol,float(self.label102Edit.text()))
                self.labelb5Edit.setText(str(R1))
                self.labelb6Edit.setText(str(R2))
                self.labelb7Edit.setText(str(R3))
                self.labelb4Edit.setText(str(C))
        else:
            self.labelbd.setText("ERROR: No ha introducido en su totalidad o no pasaron la validación")

    def standardValueEquivalent(self,val,tol):
        #LA FUNCION CALCULA VALORES DE RESISTENCIA DESDE 0.001 hasta 955000000 (955M)
        if val>=1:
            lv = [(val/(10**i)<10 and val/(10**i)>=1) for i in range(0,9)]
            mult = 10**lv.index(True)
            val = val/mult
        if val<1:
            lv = [(val/(10**(-i))<10 and val/(10**(-i))>=1) for i in range(0,12)]
            mult = 10**(-lv.index(True))
            val = val/mult

        values20 = (1.0, 1.5, 2.2, 3.3, 4.7, 6.8)

        values10 = (1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2)

        values5 = (1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, \
        3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1)

        values2 = (1.00, 1.05, 1.10, 1.15, 1.21, 1.27, 1.33, 1.40, 1.47, 1.54, \
        1.62, 1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74,\
        2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87,\
        5.11, 5.36, 5.62, 5.90, 6.19, 6.49, 6.81, 7.15, 7.50, 7.87, 8.25, 8.66,\
        9.09, 9.53)

        values1 = (1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24, \
        1.27, 1.30, 1.33, 1.37, 1.40, 1.43, 1.47, 1.50, 1.54, 1.58, 1.62, 1.65,\
        1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2.00, 2.05, 2.10, 2.15, 2.21,\
        2.26, 2.32, 2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74, 2.80, 2.87, 2.94,\
        3.01, 3.09, 3.16, 3.24, 3.32, 3.40, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92,\
        4.02, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23,\
        5.36, 5.49, 5.62, 5.76, 5.90, 6.04, 6.19, 6.34, 6.49, 6.65, 6.81, 6.98,\
        7.15, 7.32, 7.50, 7.68, 7.87, 8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31,\
        9.53, 9.76)

        values05 = (1.00, 1.01, 1.02, 1.04, 1.05, 1.06, 1.07, 1.09, 1.10, 1.11,\
        1.13, 1.14, 1.15, 1.17, 1.18, 1.20, 1.21, 1.23, 1.24, 1.26, 1.27, 1.29,\
        1.30, 1.32, 1.33, 1.35, 1.37, 1.38, 1.40, 1.42, 1.43, 1.45, 1.47, 1.49,\
        1.50, 1.52, 1.54, 1.56, 1.58, 1.60, 1.62, 1.64, 1.65, 1.67, 1.69, 1.72,\
        1.74, 1.76, 1.78, 1.80, 1.82, 1.84, 1.87, 1.89, 1.91, 1.93, 1.96, 1.98,\
        2.00, 2.03, 2.05, 2.08, 2.10, 2.13, 2.15, 2.18, 2.21, 2.23, 2.26, 2.29,\
        2.32, 2.34, 2.37, 2.40, 2.43, 2.46, 2.49, 2.52, 2.55, 2.58, 2.61, 2.64,\
        2.67, 2.71, 2.74, 2.77, 2.80, 2.84, 2.87, 2.91, 2.94, 2.98, 3.01, 3.05,\
        3.09, 3.12, 3.16, 3.20, 3.24, 3.28, 3.32, 3.36, 3.40, 3.44, 3.48, 3.52,\
        3.57, 3.61, 3.65, 3.70, 3.74, 3.79, 3.83, 3.88, 3.92, 3.97, 4.02, 4.07,\
        4.12, 4.17, 4.22, 4.27, 4.32, 4.37, 4.42, 4.48, 4.53, 4.59, 4.64, 4.70,\
        4.75, 4.81, 4.87, 4.93, 4.99, 5.05, 5.11, 5.17, 5.23, 5.30, 5.36, 5.42,\
        5.49, 5.56, 5.62, 5.69, 5.76, 5.83, 5.90, 5.97, 6.04, 6.12, 6.19, 6.26,\
        6.34, 6.42, 6.49, 6.57, 6.65, 6.73, 6.81, 6.90, 6.98, 7.06, 7.15, 7.23,\
        7.32, 7.41, 7.50, 7.59, 7.68, 7.77, 7.87, 7.96, 8.06, 8.16, 8.25, 8.35,\
        8.45, 8.56, 8.66, 8.76, 8.87, 8.98, 9.09, 9.20, 9.31, 9.42, 9.53, 9.65,\
        9.76, 9.88)

        dic = {20:values20, 10:values10, 5:values5, 2:values2, 1:values1, 0.5:values05}
        dif = [ abs(dic[tol][i]-val) for i in range(0,len(dic[tol]))]
        k = np.round(dic[tol][dif.index(min(dif))],12)
        return k*mult

    def verification(self):
        if self.comboxb1.currentIndex() == 0:
            self.label102Edit.setReadOnly(True)
            self.label102Edit.setStyleSheet("background: lightgray")
            self.label7.setText("R1a tol")
            self.label8.setText("R1b tol")
            self.label9.setText("R2 tol")
            self.labelb5.setText("R1a")
            self.labelb6.setText("R1b")
            self.labelb7.setText("R2")
            self.labelb2.setPixmap(QtGui.QPixmap(os.getcwd() + "/pb.png"))

        if self.comboxb1.currentIndex() == 1:
            self.label102Edit.setReadOnly(False)
            self.label102Edit.setStyleSheet("background: white")
            self.label7.setText("R1 tol")
            self.label8.setText("R2 tol")
            self.label9.setText("R3 tol")
            self.labelb5.setText("R1")
            self.labelb6.setText("R2")
            self.labelb7.setText("R3")
            self.labelb2.setPixmap(QtGui.QPixmap(os.getcwd() + "/pl.png"))

    def validation(self):
        dic1 = {0:20, 1:10, 2:5, 3:2, 4:1, 5:0.5}
        f=self.label3Edit.text()
        A=self.label4Edit.text()
        Q=self.label5Edit.text()
        C=self.label6Edit.text()
        indx_C_tol = self.label10Edit.currentIndex()
        C_tol_aux = dic1[indx_C_tol]
        str1 = "Alerta:"
        error = False

        if f !="":
            try:
                fn = EngNumber(f)
                if fn>EngNumber("100G") or fn < EngNumber("0"):
                    str1 += "\n" + "fo-Error: La frecuencia debe estar en el intervalo [0,100G]"
                    error = True
                else:
                    self.fn = float(fn)
            except decimal.InvalidOperation:
                str1 += "\n" + "fo-Error: Tipo de dato erroneo"
                error = True
        else:
            str1 += "\n" + "fo-Error: Introduzca un valor"
            error = True

        if A !="":
            try:
                An = EngNumber(A)
                if An>EngNumber("10k") or An < EngNumber("0"):
                    str1 += "\n" + "A-Error: La ganancia debe estar en el intervalo [0,10k]"
                    error = True
                else:
                    self.An = float(An)
            except decimal.InvalidOperation:
                str1 += "\n" + "A-Error: Tipo de dato erroneo"
                error = True
        else:
            str1 += "\n" + "A-Error: Introduzca un valor"
            error = True

        if Q !="":
            try:
                Qn = EngNumber(Q)
                if Qn>EngNumber("1k") or Qn < EngNumber("0"):
                    str1 += "\n" + "Q-Error: El factor de calidad debe estar en el intervalo [0,1k]"
                    error = True
                else:
                    self.Qn = float(Qn)
            except decimal.InvalidOperation:
                str1 += "\n" + "Q-Error: Tipo de dato erroneo"
                error = True
        else:
            str1 += "\n" + "Q-Error: Introduzca un valor"
            error = True

        if C !="":
            try:
                Cn = EngNumber(C)
                if Cn>EngNumber("10m") or Cn < EngNumber("10p"):
                    str1 += "\n" + "C-Error: El valor del condensador debe estar en el intervalo [10p,10m]"
                    error = True
                else:
                    if self.count:
                        Cn = float(Cn)
                        self.KK = Cn
                        """print("KK:{}".format(self.KK))"""
                        g = str(EngNumber(self.standardValueEquivalent(Cn,C_tol_aux)))
                        self.label6Edit.setText(g)
                        self.count = False
                        self.Cn = self.KK
                    else:
                        g = EngNumber(self.standardValueEquivalent(self.KK,C_tol_aux))
                        """print("g:{}".format(g))
                        print("KK2:{}".format(self.KK))"""
                        self.Cn = float(g)
                        self.label6Edit.setText(str(g))

            except decimal.InvalidOperation:
                str1 += "\n" + "C-Error: Tipo de dato erroneo"
                error = True
        else:
            str1 += "\n" + "C-Error: Introduzca un valor"
            error = True

        if error:
            self.labelbd.setText(str1)
        else:
            self.labelbd.setText("Datos válidos")
            self.validat = True


    def pBand(self,f,Q,A,C,tolC,tolR1a,tolR1b,tolR2):
        wo = 2*np.pi*f
        CAux = C
        R1aAux = Q/(A*wo*CAux)
        R1bAux = R1aAux/(((2*(Q**2))/(A))-1)
        R2Aux = 2*Q/(wo*CAux)
        #print("R2Aux: {}\nR1bAux: {}\nR1aAux: {}".format(R2Aux,R1bAux,R1aAux))
        C = EngNumber(self.standardValueEquivalent(C,tolC))
        R1b = EngNumber(self.standardValueEquivalent(R1bAux,tolR1b))
        R2 = EngNumber(self.standardValueEquivalent(R2Aux,tolR2))
        R1a = EngNumber(self.standardValueEquivalent(R1aAux,tolR1a))
        return C, R1a, R1b, R2

    def pLow(self,f,Q,A,C,tolC,tolR1,tolR2,tolR3,n):
        wo = 2*np.pi*f
        nC = n*C
        R3Aux = (1+np.sqrt(1-((4*Q**2)*(1+A))/(n)))/(2*wo*Q*C)
        #R3Aux = (1+np.sqrt(1-((4*Q**2)*(1+A))/(n)))/(2*wo*Q*C)
        R1Aux = R3Aux/A
        R2Aux = (1)/(wo**2*R3Aux*nC*C)

        C2 = C
        C1 = EngNumber(self.standardValueEquivalent(nC,tolC))
        R1 = EngNumber(self.standardValueEquivalent(R1Aux,tolR1))
        R2 = EngNumber(self.standardValueEquivalent(R2Aux,tolR2))
        R3 = EngNumber(self.standardValueEquivalent(R3Aux,tolR3))

        return R1, R2, R3, C
app = QtGui.QApplication(sys.argv)
qb = MainWindow()
qb.show()
sys.exit(app.exec_())
