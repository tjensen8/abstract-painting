import yaml

def load_config():
    with open("./src/config.yml") as f:
        try:
            config = yaml.safe_load(f)
            return config
        except Exception as e:
            print(e)
            return ""