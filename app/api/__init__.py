from sanic import Blueprint
from ..utils import dynamic

modules = dynamic.import_submodules(__name__, __file__)
blueprints = map(lambda m: m.bp, modules)
bp = Blueprint.group(*blueprints, url_prefix="/api")

