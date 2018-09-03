from collections import namedtuple
# Own modules
from reverse_dict import methods


class Config:
    def __init__(self):
        self.version = 0.1
        self.github_url = 'https://github.com/raul23/python_reverse_dict'
        self.methods = self._get_methods_version()

    @staticmethod
    def _get_methods_version():
        methods_ = {}
        for k, v in methods.__dict__.items():
            try:
                method_name = v.__method_name__
                method_class_name = v.__name__
            except (AttributeError, TypeError) as e:
                continue
            else:
                methods_.setdefault(method_name, method_class_name)
        return methods_


cfg = Config()

