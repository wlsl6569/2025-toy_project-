import import_character
from item_add import add_item, use_item
import time, random
import sys


name, job, item = import_character.load_character()

def start3():
    time.sleep(1)
    print(f'...고요한 새벽, {name}은 짝사랑하는 이와 만났다.')
    time.sleep(1)
    print(f'{name}: 드디어 때가 되었군요.')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(f'상대에게 선물할 아이템을 고르세요')

    items, thing = use_item()
    #print("thing: ", thing)
    

    time.sleep(1)
    print(f'{name}은 수줍은 얼굴로 {thing}을 꺼내들었다.')
    time.sleep(1)
    print(f'상대방 : {name}님, 이것의 의미는...?')
    time.sleep(1)
    print(f'{name}: 맞아요.')
    time.sleep(1)
    print(f'{name}는 {thing}를 상대방에게 건냈다.')
    time.sleep(1)
    print(f'{name}: 당신이 생각하는 게 맞습니다.')
    time.sleep(1)
    if thing == '검':
        print(f'상대방 : 그럼 결투신청을 받아들이죠.')
        time.sleep(1)
        print(f'{name}:?!')
        time.sleep(1)
        print(f'선물이 오해를 불러와 둘은 적이 되었다!')
        time.sleep(1)
        print(f'...')
        time.sleep(1)
        print(f'The End')
        return
    elif thing == '명예훈장':
        print(f'{thing}을 받은 상대방은 {name}을 바라본다.')
        time.sleep(1)
        print(f'{name} : ...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print(f'상대방 : 감사한데 마음만 받을게요.')
        time.sleep(1)
        print('상대방 : 되게 부담스럽네요.')
        time.sleep(1)
        print(f'The End')
        return


