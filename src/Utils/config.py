import json

def parse_config(path = "config.json"): 
    with open(path, "r") as f: 
        return json.load(f)

def write_config(config:dict, path="config.json") ->  None: 
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)