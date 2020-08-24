import pkgutil
from importlib import import_module
from pathlib import Path


def import_submodules(current_module_name: str, filename: str) -> list:
    modules = []
    root_pkg = Path(filename).parent
    for (file_finder, name, _) in pkgutil.iter_modules([root_pkg]):
        module = import_module(current_module_name + "." + name)
        modules.append(module)

    return modules
