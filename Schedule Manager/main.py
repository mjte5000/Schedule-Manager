import sys

from app.app import Application
from ui.main_window import MainWindow


def main():
    app = Application(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
