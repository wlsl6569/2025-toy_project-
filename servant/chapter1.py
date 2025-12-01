import json
import import_character
from item_add import add_item as additem
import time

tool = '포기하지 않는 마음'
def start():
    name, job = import_character.load_character()

    print(f'{name}은 노예시장으로 들어왔다!')
    time.sleep(0.5)

    print(f'기왕 내가 선택한 {job}... 최고의 {job}이 되어주마!')

    time.sleep(0.5)

    print(f'{name}은 {tool}이 몸 안에서 부터 차오르는 것을 느낀다.')
    time.sleep(1)
    print(f'...')

    additem(tool)


    

