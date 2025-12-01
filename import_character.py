import json

def load_character():
    with open('character_info','r') as f:
        data = json.load(f)

    return data['name'], data['job']

name, job = load_character()
