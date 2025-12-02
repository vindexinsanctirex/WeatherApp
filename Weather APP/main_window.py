# this .py is not ready, use main.py instead

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Weather App")

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather App")

        # Configurar a imagem de fundo
        background_label = QLabel(self)
        pixmap = QPixmap("sund.png")
        background_label.setPixmap(pixmap)
        background_label.setScaledContents(True)
        background_label.setGeometry(0, 0, self.width(), self.height())

 


if __name__ == "__main__":
    app = QApplication([])
    window = WeatherApp()
    window.show()
    app.exec()
