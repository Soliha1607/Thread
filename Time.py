from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QThread, QTime, QTimer, pyqtSignal
import sys

class TimeThread(QThread):
    update_time = pyqtSignal(str)

    def run(self):
        while True:
            current_time = QTime.currentTime().toString("HH:mm:ss")
            self.update_time.emit(current_time)
            self.sleep(1)

class TimeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hozirgi vaqt")
        self.setGeometry(200, 200, 300, 100)

        self.timeLabel = QLabel("Hozirgi vaqt", self)
        self.timeLabel.setGeometry(50, 30, 200, 40)

        self.thread = TimeThread()
        self.thread.update_time.connect(self.update_time)
        self.thread.start()

    def update_time(self, time_text):
        self.timeLabel.setText(time_text)

app = QApplication(sys.argv)
window = TimeWindow()
window.show()
sys.exit(app.exec())