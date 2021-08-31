import sys
from mainWindow import Main
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    widget.show()
    sys.exit(app.exec_())
