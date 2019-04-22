from PyQt4 import QtGui
from PyQt4 import QtCore
import sys
import os

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
        self.label6Edit.editingFinished.connect(self.validation)
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
        self.label10Edit.setStyleSheet(styleSheetStr)
        self.label10Edit.addItems(["E6 : 20%","E12 : 10%","E24 : 5%","E48 : 2%","E96 : 1%","E192 : 0.5%",])
        #self.label10Edit.setFixedWidth(200)
        self.grid.addWidget(self.label10Edit,12,1,1,1)

        self.label102 = QtGui.QLabel("n")
        self.label102.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.grid.addWidget(self.label102,13,0,1,1)
        self.label102Edit = QtGui.QLineEdit()
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
        #self.connect(self.boton, QtCore.SIGNAL('clicked()'),self.calcular)
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
        self.labelbd.setText("USER$")
        self.grid.addWidget(self.labelbd,14,0,1,4)
        #self.labelbd.setFixedWidth(800)
        self.labelbd.setFixedHeight(200)

        #self.setFixedWidth(800)
        #self.setMinimumWidth(800)
        self.setMinimumWidth(1000)
        self.setLayout(self.grid)
        self.showMaximized()

    def verification(self):
        if self.comboxb1.currentIndex() == 0:
            self.label102Edit.setReadOnly(False)
            self.label102Edit.setStyleSheet("background: white")
            self.label7.setText("R1a tol")
            self.label8.setText("R1b tol")
            self.label9.setText("R2 tol")
            self.labelb5.setText("R1a")
            self.labelb6.setText("R1b")
            self.labelb7.setText("R2")
            self.labelb2.setPixmap(QtGui.QPixmap(os.getcwd() + "/pb.png"))

        if self.comboxb1.currentIndex() == 1:
            self.label102Edit.setReadOnly(True)
            self.label102Edit.setStyleSheet("background: lightgray")
            self.label7.setText("R1 tol")
            self.label8.setText("R2 tol")
            self.label9.setText("R3 tol")
            self.labelb5.setText("R1")
            self.labelb6.setText("R2")
            self.labelb7.setText("R3")
            self.labelb2.setPixmap(QtGui.QPixmap(os.getcwd() + "/pl.png"))

    def validation(self):
        print("RUEDALA CHAMITO")

app = QtGui.QApplication(sys.argv)
qb = MainWindow()
qb.show()
sys.exit(app.exec_())
