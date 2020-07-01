import subprocess


class SetUp:
    """
    This class is responsible for the dependencies that are required to run
    the App.
    it check if need to install the relevant packages
    """
    PACKAGES = ['bottle', 'requests', 'json', 'datetime', 'numpy']

    def __init__(self):
        for package in self.PACKAGES:
            self.install(package)

    @staticmethod
    def install(package):
        """
        This method ensure that the user will have all the packages that
        are required to run this program
        :param package:
        :return:
        """
        import importlib
        try:
            importlib.import_module(package)
        except ImportError:
            subprocess.call(['pip3', 'install', package])
