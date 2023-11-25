import os
from PyQt5.QtCore import QFile, QTextStream


# create a class for theme managing
class ThemeManager:
    def __init__(self, application):
        self.application = application

    # function to apply theme
    def applyTheme(self, theme_name):
        theme_file = os.path.join("resources", "themes", f"{theme_name}_theme.qss")
        if os.path.exists(theme_file):
            with open(theme_file, "r") as file:
                self.application.setStyleSheet(file.read())
        else:
            print(f"Theme file {theme_file} not found")
