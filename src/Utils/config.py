import json
from pathlib import Path

def parse_config(path = Path(__file__).resolve().parent.joinpath("../../config.json")): 
    print("Reading config")
    with open(path, "r") as f: 
        return json.load(f)

def write_config(config:dict, path="config.json") ->  None: 
    print("Writing config")
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)