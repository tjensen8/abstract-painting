import yaml

def load_config():
    with open("./src/config.yml") as f:
        try:
            config = yaml.safe_load(f)
            print("Config Loaded Successfully")
            return config
        except Exception as e:
            print(e)
            return ""

if __name__ == '__main__':
    load_config()