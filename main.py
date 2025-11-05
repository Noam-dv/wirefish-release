from app import WireFish
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    print("app running 8)")
    app = QApplication(sys.argv)
    w = WireFish()
    w.show()
    sys.exit(app.exec())