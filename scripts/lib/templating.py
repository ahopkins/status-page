from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(loader=PackageLoader("lib", "templates"), autoescape=select_autoescape(["md"]))
