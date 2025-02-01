from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtCore import QThread, pyqtSignal
import sys
import random

class ColorThread(QThread):
    update_color = pyqtSignal(str)

    def run(self):
        color = "#{:02x}{:02x}{:02x}".format(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.update_color.emit(color)

class ColorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tasodifiy rang generatori")
        self.setGeometry(200, 200, 300, 150)

        self.colorLabel = QLabel("Rang", self)
        self.colorLabel.setGeometry(50, 30, 200, 50)
        self.colorLabel.setStyleSheet("background-color: #ffffff;")

        self.refreshButton = QPushButton("Yangilash", self)
        self.refreshButton.setGeometry(100, 90, 100, 30)
        self.refreshButton.clicked.connect(self.start_color_change)

        self.thread = ColorThread()
        self.thread.update_color.connect(self.update_color)

    def start_color_change(self):
        self.thread.start()

    def update_color(self, color_code):
        self.colorLabel.setStyleSheet(f"background-color: {color_code};")

app = QApplication(sys.argv)
window = ColorWindow()
window.show()
sys.exit(app.exec())
