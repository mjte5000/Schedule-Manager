from PyQt6.QtWidgets import QApplication


class Application(QApplication):
    """
    Creates an application for the GUI to run in.
    :cvar _instance: the single instance of the `Application`
    """

    _instance = None

    def __new__(cls, argv: list[str]):
        """
        Creates the single instance of the `Application`
        :param argv: command line arguments
        """
        if cls._instance is None:
            cls._instance = super(Application, cls).__new__(cls)
        return cls._instance

    def __init__(self, argv: list[str]):
        """
        Constructs an `Application` object with the required attributes.
        :param argv: command line arguments
        """
        super().__init__(argv)

    def instance(self):
        """
        Returns the single instance of the `Application`.
        :return: the single instance of the `Application`
        :raises RuntimeError: if the `Application` instance has not been created
        """
        if self._instance is None:
            raise RuntimeError('Application instance has not been created')
        return self._instance
