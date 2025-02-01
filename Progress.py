from PyQt6.QtWidgets import QApplication, QMainWindow, QProgressBar, QPushButton
from PyQt6.QtCore import QThread, pyqtSignal
import sys
import time

class ProgressThread(QThread):
    update_progress = pyqtSignal(int)

    def run(self):
        for i in range(101):
            self.update_progress.emit(i)
            time.sleep(0.1)

class ProgressBarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress barni yangilash")
        self.setGeometry(200, 200, 400, 150)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(50, 30, 300, 30)

        self.startButton = QPushButton("Ishni boshlash", self)
        self.startButton.setGeometry(150, 80, 100, 30)
        self.startButton.clicked.connect(self.start_progress)

        self.thread = ProgressThread()
        self.thread.update_progress.connect(self.update_progress)

    def start_progress(self):
        self.thread.start()

    def update_progress(self, value):
        self.progressBar.setValue(value)

app = QApplication(sys.argv)
window = ProgressBarWindow()
window.show()
sys.exit(app.exec())
