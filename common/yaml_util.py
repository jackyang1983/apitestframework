import yaml


class YamlUtil:
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def read(self):
        with open(self.yaml_file, mode="r", encoding="utf-8") as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    def write(self, data):
        with open(self.yaml_file, mode="a", encoding="utf-8") as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    def clean(self):
        with open(self.yaml_file, mode="w", encoding="utf-8") as f:
            f.truncate()
