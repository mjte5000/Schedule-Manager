from PyQt6.QtWidgets import QApplication


class Application(QApplication):

    def __init__(self, argv: list[str]):
        super().__init__(argv)