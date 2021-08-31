from ui_form import Ui_Main
from PySide6.QtWidgets import QApplication, QWidget
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

        self.graph = pg.PlotWidget()
        self.graph.showGrid(x=True, y=True)
        self.graph.setXRange(-5, 5)
        self.graph.setYRange(-5, 5)
        self.ui.Grid.setScene(self.graph)

