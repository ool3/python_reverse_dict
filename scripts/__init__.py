import pkgutil
scripts_lookup = {}
for f, name, _ in pkgutil.iter_modules(['scripts']):
    scripts_module = __import__('{}.{}'.format(f.path, name))
    method_module = scripts_module.__getattribute__(name)
    method_name = method_module.method_name
    scripts_lookup.setdefault(method_name, method_module)
