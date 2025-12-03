import import_character
from item_add import add_item, use_item
import time, random
import sys


name, job, item = import_character.load_character()

def start3():
    time.sleep(1)
    print(f'...다음 날 연회장, {name}은 친구들에게 둘러쌓여 있다.')
    time.sleep(1)
    print(f'{name}: 친구들 앞에서 꺼내놓고 싶어졌다.')
    time.sleep(1)

    items, thing = use_item()
    #print("thing: ", thing)
    

    time.sleep(1)
    print(f'{name}은 친구들 앞에 {thing}를 꺼내놓는다.')
    time.sleep(1)
    print(f'{name}: 오래전부터 이걸 보여주고 싶었지.')
    time.sleep(1)
    print(f'친구들이 놀란 눈으로 {name}을 바라본다.')
    time.sleep(1)
    if thing == '와인':
        print(f'친구들 : 우와앗, 이건 최고급 {thing}...!')
        print(f'{name}: 맞아. 너희와 먹는다면 그 순간만큼은 즐겁겠지..')
        time.sleep(1)
        print(f'...')
        time.sleep(1)
        print(f'The End')
        return
    elif thing == '우울증':
        print(f'친구들: 언제부터 이렇게 슬펐던거냐고!')
        time.sleep(1)
        print(f'...')
        time.sleep(1)
        print(f'{name}: 크흐흑, 사실은 그게...')
        time.sleep(1)
        print(f'...')
        time.sleep(1)
        print(f'{name}은 깊은 속얘기들을 시작했다.')
        time.sleep(1)
        print(f'{name}은 오랜만에 안정감을 느꼈다.')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print(f'The End')
        return


