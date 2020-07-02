import subprocess


class SetUp:
    """
    This class is responsible for the dependencies that are required to run
    the App.
    it check if need to install the relevant packages
    """
    PACKAGES_3 = ['bottle', 'requests', 'json', 'datetime', 'pytest']
    PACKAGES_2 = ['numpy']

    def __init__(self):
        for package in self.PACKAGES_3:
            self.install(package)
        for package in self.PACKAGES_2:
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
            subprocess.call(['sudo', 'pip3', 'install', package])


if __name__ == '__main__':
    SetUp()
