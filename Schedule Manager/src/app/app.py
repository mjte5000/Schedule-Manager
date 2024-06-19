from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication

from .config import Config


class Application(QApplication):
    """
    Creates an application for the GUI to run in.
    """

    def __init__(self, argv: list[str]):
        """
        Constructs an `Application` object with the required attributes.
        :param argv: command line arguments
        """
        super().__init__(argv)

        self.setApplicationName("Schedule Manager")
        self.setWindowIcon(QIcon(Config.App.icon))
        with open(Config.App.style) as f:
            style = f.read()
        self.setStyleSheet(style)

    @staticmethod
    def instance() -> QCoreApplication | None:
        """
        Returns the single instance of the `Application`.
        :return: the single instance of the `Application` or `None` if no instance has been created
        """
        return QApplication.instance()
