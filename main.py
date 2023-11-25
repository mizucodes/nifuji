from PyQt5.QtWidgets import QApplication
from mainWindow import MainWindow  # Import the MainWindow class
from themeManager import ThemeManager
import sys


def nifuji():
    app = QApplication(sys.argv)  # Create an application object
    mainWindow = MainWindow()  # Create an instance of MainWindow
    mainWindow.show()  # Show the main window
    sys.exit(app.exec_())  # Start the application's main loop


if __name__ == "__main__":
    nifuji()
