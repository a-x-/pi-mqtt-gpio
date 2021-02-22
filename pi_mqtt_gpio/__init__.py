import yaml

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

CONFIG_SCHEMA = read('../config.schema.yml')
