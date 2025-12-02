import import_character
from item_add import add_item 
import time, random


name, job, item = import_character.load_character()

def start3():
    time.sleep(1)
    print('...고요한 저녁, {name}은 모닥불을 바라보며 앉아있다.')
    time.sleep(1)
    print('{name}: 열심히 일했더니 출출하군.')
    time.sleep(1)

    