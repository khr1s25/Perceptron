from PySide6.QtCore import Slot

import ui_form
from PySide6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsSceneMouseEvent
from random import randint
import pyqtgraph as pg
import numpy as np
from PySide6.QtGui import QPen,QColor, QMouseEvent, Qt

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui_form.Ui_Main()
        self.ui.setupUi(self)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 386, 286)
        self.ui.Grid.setScene(self.scene)
        self.graph = pg.plot()
        self.graph.setGeometry(6, 6, 380, 280)
        self.graph.showGrid(x=True, y=True)
        self.graph.setXRange(5, -5)
        self.graph.setYRange(5, -5)
        self.scene.addWidget(self.graph)
        self.scene.mousePressEvent = self.click

        # _____--------______---------_________---------________________________--------------

    # def perceptron(self):
    #     for _ in range(self.masIter):
    #         for idx, x_i in enumerate(self.samples):
    #             salidaLinear = np.dot(x_i, self.pesos) + self.salidas
    #             tipoPredecido = self.funcionActivacion(salidaLinear)
    #
    #             update = self.learningRate * (self.tipos[idx] - tipoPredecido)
    #             self.pesos += update * x_i
    #
    #
    # def prueba(self):
    #     pass
    #
    # def prediccion(self):
    #     salidaLinear =  np.dot(self.samples, self.pesos) + self.salidas
    #     tipoPredecido = self.funcionActivacion(salidaLinear)
    #     return tipoPredecido
    #
    # def funcionActivacion(self, x):
    #     return np.where(x>=0, 1, 0)
    #
    # @Slot()
    # def iniciarPesos(self):
    #     self.pesos = np.random(self.n_features)
    #     self.salidas = 0
    #
    # @Slot()
    # def click(self, event):
    #     pen = QPen()
    #     x = event.scenePos().x()
    #     y = event.scenePos().y()
    #     coordenada = {
    #         "x": x,
    #         "y": y
    #     }
    #     pen.setWidth(2)
    #     if self.ui.tipo1.isChecked():
    #         pen.setColor("green")
    #         self.samples.append(coordenada)
    #         self.tipos.append(1)
    #     elif self.ui.tipo2.isChecked():
    #         pen.setColor("red")
    #         self.samples.append(coordenada)
    #         self.tipos.append(0)
    #     self.scene.addEllipse(x, y, 4, 4, pen)
