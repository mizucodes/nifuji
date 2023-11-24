from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
import sys


# main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # configuration of the window
        self.setWindowTitle("nifuji")  # title of window
        self.setGeometry(100, 100, 800, 600)  # size of window

        # set the main widget
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)


def nifuji():
    app = QApplication(sys.argv)  # this creates a application object
    mainWindow = MainWindow()  # creates an instance of the main window
    mainWindow.show()  # show the actual main window
    sys.exit(app.exec_())  # starts the applications main loop


if __name__ == "__main__":
    nifuji()
