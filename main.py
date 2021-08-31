# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import pyqtgraph as pg
from pyqtgraph import PlotWidget, plot

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Main()
    widget.show()
    sys.exit(app.exec_())
