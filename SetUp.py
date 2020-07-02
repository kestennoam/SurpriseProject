import subprocess
import sys


class SetUp:
    """
    This class is responsible for the dependencies that are required to run
    the App.
    it check if need to install the relevant packages
    """
    PACKAGES_3 = ['bottle', 'requests', 'json', 'datetime', 'pytest']
    PACKAGES_2 = ['numpy', 'pytest']

    def __init__(self):
        version = 'pip' + str(sys.version_info[0])
        for package in self.PACKAGES_3:
            self.install(package, version)
        for package in self.PACKAGES_2:
            self.install(package, 'pip')

    @staticmethod
    def install(package, version):
        """
        This method ensure that the user will have all the packages that
        are required to run this program
        :param version: version of python
        :param package: package to install as string
        :return:
        """
        import importlib
        try:
            importlib.import_module(package)
        except ImportError:
            subprocess.call(['sudo', version, 'install', package])


if __name__ == '__main__':
    SetUp()
