import subprocess


class SetUp:
    PACKAGES = ['bottle', 'requests', 'json']

    def __init__(self):
        for package in self.PACKAGES:
            self.install_and_import(package)

    @staticmethod
    def install_and_import(package):
        import importlib
        try:
            importlib.import_module(package)
        except ImportError:
            subprocess.call(['pip3', 'install', package])
