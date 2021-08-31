from ui_form import Ui_Main
from PySide6.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene
import os
from pathlib import Path
import sys
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        # pen = pg.mkPen(color=())
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 386, 286)
        self.ui.Grid.setScene(self.scene)

        self.graph = pg.plot()
        self.graph.setGeometry(6, 6, 380, 280)
        self.graph.showGrid(x=True, y=True)
        self.graph.setXRange(5, -5)
        self.graph.setYRange(5, -5)
        self.scene.addWidget(self.graph)


