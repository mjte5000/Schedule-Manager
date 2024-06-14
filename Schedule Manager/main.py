import sys

from src.app.app import Application
from src.ui.main_window import MainWindow


def main():
    app = Application(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
