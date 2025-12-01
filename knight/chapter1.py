import json
from import_character import load_character



def start():
    name, job = load_character()

    print(f'{name}은 훈련장으로 들어왔다!')

