from ui_form import Ui_Main
from PySide6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene
from random import randint
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from PySide6.QtGui import QPen,QColor, QMouseEvent, Qt
from punto import Punto

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
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
