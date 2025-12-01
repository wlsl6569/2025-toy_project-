import json
import import_character

def start():
    name, job = import_character.load_character()

    print(f'{name}은 밭으로 들어왔다!')

