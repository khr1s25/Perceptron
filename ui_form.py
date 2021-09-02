# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.gridLayout = QGridLayout(Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Epoca = QListWidget(Main)
        self.Epoca.setObjectName(u"Epoca")

        self.gridLayout.addWidget(self.Epoca, 3, 0, 1, 1)

        self.widget = QWidget(Main)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tipo2 = QRadioButton(self.widget)
        self.tipo2.setObjectName(u"tipo2")

        self.gridLayout_3.addWidget(self.tipo2, 5, 0, 1, 1)

        self.learnigRate = QDoubleSpinBox(self.widget)
        self.learnigRate.setObjectName(u"learnigRate")
        self.learnigRate.setDecimals(1)
        self.learnigRate.setMinimum(0.100000000000000)
        self.learnigRate.setMaximum(0.900000000000000)
        self.learnigRate.setSingleStep(0.100000000000000)

        self.gridLayout_3.addWidget(self.learnigRate, 3, 0, 1, 1)

        self.iniciarPerceptron = QPushButton(self.widget)
        self.iniciarPerceptron.setObjectName(u"iniciarPerceptron")

        self.gridLayout_3.addWidget(self.iniciarPerceptron, 5, 1, 1, 1)

        self.epocasMax = QSpinBox(self.widget)
        self.epocasMax.setObjectName(u"epocasMax")
        self.epocasMax.setMinimum(1)
        self.epocasMax.setMaximum(9999999)

        self.gridLayout_3.addWidget(self.epocasMax, 0, 0, 1, 1)

        self.tipo1 = QRadioButton(self.widget)
        self.tipo1.setObjectName(u"tipo1")
        self.tipo1.setChecked(True)

        self.gridLayout_3.addWidget(self.tipo1, 4, 0, 1, 1)

        self.iniciarPesos = QPushButton(self.widget)
        self.iniciarPesos.setObjectName(u"iniciarPesos")

        self.gridLayout_3.addWidget(self.iniciarPesos, 4, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.Error = QGraphicsView(Main)
        self.Error.setObjectName(u"Error")

        self.gridLayout.addWidget(self.Error, 3, 1, 1, 1)

        self.Grid = QGraphicsView(Main)
        self.Grid.setObjectName(u"Grid")
        self.Grid.setMinimumSize(QSize(386, 286))
        self.Grid.setMaximumSize(QSize(386, 286))
        self.Grid.setMouseTracking(True)

        self.gridLayout.addWidget(self.Grid, 0, 0, 1, 1)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Main", None))
        self.tipo2.setText(QCoreApplication.translate("Main", u"Tipo 2", None))
        self.iniciarPerceptron.setText(QCoreApplication.translate("Main", u"Perceptron", None))
        self.tipo1.setText(QCoreApplication.translate("Main", u"Tipo 1", None))
        self.iniciarPesos.setText(QCoreApplication.translate("Main", u"Iniciar pesos", None))
    # retranslateUi

