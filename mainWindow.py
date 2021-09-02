from PySide6.QtCore import Slot

import ui_form
from perceptron import Perceptron
from PySide6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsSceneMouseEvent
import pyqtgraph as pg
import numpy as np
from PySide6.QtGui import QPen,QColor, QMouseEvent, Qt

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.samples = []
        self.tipos = []
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

        self.pesos = np.zeros(self.samples)

        self.p = Perceptron(float(self.ui.learnigRate.text()), int(self.ui.epocasMax.text()), self.pesos)
        self.ui.iniciarPesos.clicked.connect(self.iniciarPesos)
        self.ui.iniciarPerceptron.clicked.connect(self.iniciarPerceptron)

    @Slot()
    def click(self, event):
        pen = QPen()
        x = event.scenePos().x()
        y = event.scenePos().y()
        coordenada = {
            "x": x,
            "y": y
        }
        pen.setWidth(2)
        if self.ui.tipo1.isChecked():
            pen.setColor("green")
            self.samples.append(coordenada)
            self.tipos.append(1)
        elif self.ui.tipo2.isChecked():
            pen.setColor("red")
            self.samples.append(coordenada)
            self.tipos.append(0)
        self.scene.addEllipse(x, y, 4, 4, pen)

    @Slot()
    def iniciarPesos(self):
        pass

    def iniciarPerceptron(self):
        self.p.fit(self.samples, self.tipos)
