import json

def load_character():
    with open('character_info','r',encoding='utf-8') as f:
        data = json.load(f)

    return data['name'], data['job']

name, job = load_character()
