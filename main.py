import sys
import mainWindow
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication([])
    widget = mainWindow.Main()
    widget.show()
    sys.exit(app.exec_())
