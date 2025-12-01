import json
import import_character
from item_add import add_item as additem
import time

tool = '삽'
def start():
    name, job = import_character.load_character()

    print(f'{name}은 밭으로 들어왔다!')

    time.sleep(0.5)

    print(f'기왕 내가 선택한 {job}... 최고의 {job}이 되어주마!')

    time.sleep(0.5)

    print(f'{name}은 {tool}을 얻었다!')
    time.sleep(0.5)

    additem(tool)
    

    

