from jinja2 import Template, Environment, FileSystemLoader
from ruamel.yaml import YAML
from pathlib import Path

yml_data = 'data.yml'
yaml = YAML(typ='safe')
path = Path(yml_data)
data = yaml.load(path)
filename = 'sample.c.template'

# https://www.python.ambitious-engineer.com/archives/776
env = Environment(loader=FileSystemLoader(
    '.'), trim_blocks=True, lstrip_blocks=True)
t = env.get_template(filename)
d = t.render(data)
print(d)
