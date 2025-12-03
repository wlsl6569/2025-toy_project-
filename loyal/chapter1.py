import json
from loyal.chapter2 import start2

import import_character
from item_add import add_item as additem
import time

tool = '와인병'

def start():
    name, job, item = import_character.load_character()

    print(f'{name}은 대저택으로 들어왔다!')

    time.sleep(1)

    print(f'기왕 내가 선택한 {job}... 최고의 {job}이 되어주마!')

    time.sleep(1)

    print('...?')

    time.sleep(1)

    print(f'{name}은 첩이 들고있던 {tool}을 발견했다.')
    time.sleep(1)

    additem(tool)

    time.sleep(1)
    print('이제 얼큰하게 부패해볼까? \n select Y(yes) or N(no)')

    time.sleep(0.5)
    select = input('>>>')
    if select in ['N','n','no','NO','No']:
        print(f'{name}은 정신을 차리고 나라에 도움이 되는 정의로운 귀족이 되었다.')
        return
    
    elif select in ['Y','YES','Yes','yes','y']:
        time.sleep(1)
        print('대저택에 술냄새가 진동한다...')
        time.sleep(1)
        print(f'{name}: 최고의 타락을 보여주마!')

        time.sleep(2)
        print('...')
        time.sleep(1)
        print(f'{name}: 이제 노는 방법을 알아봐야겠어.')
        time.sleep(1)
        print('놀이 방법 : 오전에는 W키를 눌러 보석을 사들여. 오후에는 A키를 눌러 폭식을 하고 저녁에는 D키를 눌러 술을 마셔. 마지막으로 자괴감이 올라오면 S키를 눌러 기부를 해봐! ')
        time.sleep(1)
        print(f'{name}: 준비됐으면 이제 enter키를 눌러 유흥을 시작하자!')

        x = input()

        if x == "":
            start2()


    

    

    

