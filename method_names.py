class MethodNames:
    def __init__(self):
        self.main_script = 'main_script'
        self.method_01_py2 = 'method_01_py2'
        self.method_01_py3 = 'method_01_py3'
        self.method_02_py2 = 'method_02_py2'
        self.method_02_py3 = 'method_02_py3'
        self.method_03_py2 = 'method_03_py2'
        self.method_03_py3 = 'method_03_py3'

    def get_01_methods(self):
        return [self.method_01_py2, self.method_01_py3]

    def get_02_methods(self):
        return [self.method_02_py2, self.method_02_py3]

    def get_03_methods(self):
        return [self.method_03_py2, self.method_03_py3]


method_names = MethodNames()