from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    """
    Creates the main window for the application.
    :ivar menu_bar: the menu bar
    :ivar file_menu: contains actions involving files
    :ivar load_employees_action: click to load employees from a file
    :ivar save_employees_action: click to save employees to a file
    :ivar central_widget: the central widget of the window
    """

    def __init__(self):
        """
        Constructs a `MainWindow` object with the required attributes.
        """
        super().__init__()

        self.setWindowTitle("Schedule Manager")

        # Menu bar
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # Menu bar > File
        self.file_menu = QMenu("File", self)
        self.menu_bar.addMenu(self.file_menu)

        # Menu bar > File > Load Employees from File
        self.load_employees_action = QAction("Load Employees from File", self)
        self.load_employees_action.triggered.connect(self.load_employees)
        self.file_menu.addAction(self.load_employees_action)

        # Menu bar > File > Save Employees to File
        self.save_employees_action = QAction("Save Employees to File", self)
        self.save_employees_action.triggered.connect(self.save_employees)
        self.file_menu.addAction(self.save_employees_action)

        # Central widget
        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)

    def load_employees(self):
        """
        Loads employees from a file into the application.
        """
        pass

    @staticmethod
    def save_employees(self):
        """
        Saves employees loaded into the application to a file.
        """
        pass


class CentralWidget(QWidget):

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
