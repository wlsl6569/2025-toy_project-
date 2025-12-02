import json
from farmer.chapter2 import start2
import import_character
from item_add import add_item as additem
import time

tool = '삽'
def start():
    name, job, item = import_character.load_character()

    print(f'{name}은 밭으로 들어왔다!')

    time.sleep(0.5)

    print(f'기왕 내가 선택한 {job}... 최고의 {job}이 되어주마!')

    time.sleep(0.5)

    print(f'{name}은 땅바닥에서 {tool}을 발견했다.')
    time.sleep(0.5)

    additem(tool)

    time.sleep(1)
    print('이제 농사를 지어볼까? /n select Y(yes) or N(no)')

    time.sleep(0.5)
    select = input('>>>')
    if select in ['N','n','no','NO','No']:
        print(f'{name}은 굶어 죽었다.')
        return
    
    elif select in ['Y','YES','Yes','yes','y']:
        print('감자야 자라나라~')
        time.sleep(1)
        print('감자의 싹이 자라났다.')
        time.sleep(1)
        print(f'{name}: 최고의 감자를 키워내마!')

        time.sleep(2)
        print('...')
        time.sleep(1)
        print(f'{name}: 이제 농사방법을 알아봐야겠어.')
        time.sleep(1)
        print('농사 방법 : 오전에는 W키를 눌러 광합성을, 오후에는 A키를 눌러 물을 주고 저녁에는 D키를 눌러 온도를 유지해줘. 마지맞으로 밤에는 S키를 눌러 감자에게 사랑한다 말해봐! ')
        time.sleep(1)
        print(f'{name}: 준비됐으면 이제 enter키를 눌러 농사를 시작하자!')

        x = input()

        if x == "":
            start2()


    

    

    

