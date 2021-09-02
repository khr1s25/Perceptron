from PySide6.QtCore import Slot

import ui_form
from PySide6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsSceneMouseEvent
from random import randint
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from PySide6.QtGui import QPen,QColor, QMouseEvent, Qt
from punto import Punto

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = ui_form.Ui_Main()
        self.ui.setupUi(self)
        self.trainingSet = []
        self.weights = []

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

        self.ui.iniciarPesos.clicked.connect(self.iniciarPesos)

    def perceptron(self):
       weight = randint(-5, 5)
       n = int(self.ui.Eta)
       done = False
       while done == False:
           done = True
           for punto in self.trainingSet:

               error = punto.tipo - self.pw(punto,weight)
               if error != 0:
                    done = False
                    w = w + n * error * punto


    def pw(self,point,w):

        if point * w >= 0:
            return 1
        else:
            return 0

    @Slot()
    def iniciarPesos(self):
        pass

    @Slot()
    def click(self, event):
        pen = QPen()
        x = event.scenePos().x()
        y = event.scenePos().y()
        pen.setWidth(2)
        if self.ui.tipo1.isChecked():
            pen.setColor("green")
        elif self.ui.tipo2.isChecked():
            pen.setColor("red")
        self.scene.addEllipse(x, y, 2, 2, pen)
