from PyQt5.QtWidgets import QAction, QFileDialog, qApp
from PyQt5.QtGui import QKeySequence


class MenuBar:
    def __init__(self, parent):
        self.parent = parent
        self.textEdit = parent.textEdit
        self.createMenuBar()

    def createMenuBar(self):
        menuBar = self.parent.menuBar()

        # File menu
        fileMenu = menuBar.addMenu("File")

        # Open action
        openAction = QAction("Open", self.parent)
        openAction.setShortcut(QKeySequence.Open)  # shortcut to Command+O
        openAction.triggered.connect(self.openFile)
        fileMenu.addAction(openAction)

        # Save action
        saveAction = QAction("Save", self.parent)
        saveAction.setShortcut(QKeySequence.Save)  # shortcut to Command+S
        saveAction.triggered.connect(self.saveFile)
        fileMenu.addAction(saveAction)

        # Exit action
        exitAction = QAction("Exit", self.parent)
        exitAction.setShortcut(QKeySequence.Quit)  # shortcut to Command+Q
        exitAction.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAction)

        # Edit menu
        editMenu = menuBar.addMenu("Edit")

        # Zoom In
        zoomInAction = QAction("Zoom In", self.parent)
        zoomInAction.setShortcut("Ctrl++")
        zoomInAction.triggered.connect(self.zoomIn)
        editMenu.addAction(zoomInAction)

        # Zoom Out
        zoomOutAction = QAction("Zoom Out", self.parent)
        zoomOutAction.setShortcut("Ctrl+-")
        zoomOutAction.triggered.connect(self.zoomOut)
        editMenu.addAction(zoomOutAction)

        # Add a 'Themes' menu
        themesMenu = self.parent.menuBar().addMenu("Themes")

        # Add 'Dark Theme' action
        darkThemeAction = QAction("Dark Theme", self.parent)
        darkThemeAction.triggered.connect(lambda: self.parent.applyTheme("dark"))
        themesMenu.addAction(darkThemeAction)

        # Add 'Light Theme' action
        lightThemeAction = QAction("Light Theme", self.parent)
        lightThemeAction.triggered.connect(lambda: self.parent.applyTheme("light"))
        themesMenu.addAction(lightThemeAction)

        # Add 'Warm Theme' action
        warmThemeAction = QAction("Warm Theme", self.parent)
        warmThemeAction.triggered.connect(lambda: self.parent.applyTheme("warm"))
        themesMenu.addAction(warmThemeAction)

        # Add 'Ayu Mirage' action
        ayumirageThemeAction = QAction("Ayu Mirage Theme", self.parent)
        ayumirageThemeAction.triggered.connect(
            lambda: self.parent.applyTheme("ayumirage")
        )
        themesMenu.addAction(ayumirageThemeAction)

    def openFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self.parent,
            "Open File",
            "",
            "Text Files (*.txt);;All Files (*)",
            options=options,
        )
        if fileName:
            with open(fileName, "r") as file:
                self.textEdit.setText(file.read())

    def saveFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(
            self.parent,
            "Save File",
            "",
            "Text Files (*.txt);;All Files (*)",
            options=options,
        )
        if fileName:
            with open(fileName, "w") as file:
                file.write(self.textEdit.toPlainText())

    def zoomIn(self):
        font = self.textEdit.font()
        font.setPointSize(font.pointSize() + 1)
        self.textEdit.setFont(font)

    def zoomOut(self):
        font = self.textEdit.font()
        font.setPointSize(max(font.pointSize() - 1, 1))
        self.textEdit.setFont(font)
