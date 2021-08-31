from ui_form import Ui_Main
from PySide6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene
import sys
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot
from PySide6.QtGui import QPen,QColor, QMouseEvent, Qt
from punto import Punto

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.lista = []

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 386, 286)
        self.ui.Grid.setScene(self.scene)

        self.graph = pg.plot()
        self.graph.setGeometry(6, 6, 380, 280)
        self.graph.showGrid(x=True, y=True)
        self.graph.setXRange(5, -5)
        self.graph.setYRange(5, -5)
        self.scene.addWidget(self.graph)

    def onCLick(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            pluma = QPen()
            pluma.setColor("g")
            coordenada = {
                "x": int(QMouseEvent.x()),
                "y": int(QMouseEvent.x())
            }
            tipo = 0

            punto = Punto()
            punto.coordenada = coordenada
            punto.tipo = tipo
            self.lista.append(punto)

