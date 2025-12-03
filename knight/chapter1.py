import json
from knight.chapter2 import start2

import import_character
from item_add import add_item as additem
import time

tool = '검'

def start():
    name, job, item = import_character.load_character()

    print(f'{name}은 훈련장으로 들어왔다!')

    time.sleep(1)

    print(f'기왕 내가 선택한 {job}... 최고의 {job}이 되어주마!')

    time.sleep(1)

    print('...?')

    time.sleep(1)

    print(f'{name}은 자신의 허리춤에서 {tool}을 꺼내든다.')
    time.sleep(1)

    additem(tool)

    time.sleep(1)
    print('이제 진정한 기사가 되어볼까? \n select Y(yes) or N(no)')

    time.sleep(0.5)
    select = input('>>>')
    if select in ['N','n','no','NO','No']:
        print(f'{name}은 성에서 쫓겨났다.')
        return
    
    elif select in ['Y','YES','Yes','yes','y']:
  
        time.sleep(1)
        print('마음 속 긍지가 느껴진다.')
        time.sleep(1)
        print(f'{name}: 최고의 기사가 되어주마!')

        time.sleep(2)
        print('...')
        time.sleep(1)
        print(f'{name}: 이제 훈련 방법을 알아봐야겠어.')
        time.sleep(1)
        print('훈련 방법 : 오전에는 W키를 눌러 검술 훈련을, 오후에는 A키를 눌러 마을 봉사를 하고 저녁에는 D키를 눌러 적군을 도발해. 마지막으로 검이 망가지면 S키를 눌러 검을 수리해봐! ')
        time.sleep(1)
        print(f'{name}: 준비됐으면 이제 enter키를 눌러 훈련를 시작하자!')

        x = input()

        if x == "":
            start2()


    

    

    

