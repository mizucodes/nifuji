from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QTextEdit,
    QAction,
    qApp,
    QFileDialog,
)
from PyQt5.QtGui import QKeySequence, QIcon
import sys


# main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window icon
        self.setWindowIcon(QIcon("resources/logo.png"))

        # configuration of the window
        self.setWindowTitle("nifuji")  # title of window
        self.setGeometry(100, 100, 800, 600)  # size of window

        # set the main widget
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        # create menu bar
        self.createMenuBar()

    def createMenuBar(self):
        menuBar = self.menuBar()

        # file menu
        fileMenu = menuBar.addMenu("File")

        # open action
        openAction = QAction("Open", self)
        openAction.setShortcut(QKeySequence.Open)  # shortcut to Command+O
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        # save action
        saveAction = QAction("Save", self)
        saveAction.setShortcut(QKeySequence.Save)  # shortcut to Command+S
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        # exit action to exit the application
        exitAction = QAction("Exit", self)
        exitAction.setShortcut(QKeySequence.Quit)  # shortcut to Command+Q
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Text Files (*.txt);;All Files (*)", options=options
        )
        if fileName:
            with open(fileName, "r") as file:
                self.textEdit.setText(file.read())

    def saveFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options
        )
        if fileName:
            with open(fileName, "w") as file:
                file.write(self.textEdit.toPlainText())


def nifuji():
    app = QApplication(sys.argv)  # this creates a application object
    mainWindow = MainWindow()  # creates an instance of the main window
    mainWindow.show()  # show the actual main window
    sys.exit(app.exec_())  # starts the applications main loop


if __name__ == "__main__":
    nifuji()
