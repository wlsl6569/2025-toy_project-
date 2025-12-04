import json
from king.chapter2 import start2

import import_character
from item_add import add_item as additem
import time

tool = '왕의 지팡이'

def start():
    name, job, item = import_character.load_character()

    print(f'{name}은 성으로 들어왔다!')

    time.sleep(1)

    print(f'기왕 내가 선택한 {job}... 최고의 {job}이 되어주마!')

    time.sleep(1)

    print('...?')

    time.sleep(1)

    print(f'{name}은 시종에게서 {tool}을 받는다.')
    time.sleep(1)

    additem(tool)

    time.sleep(1)
    print('이제 나라일을 해볼까? \n select Y(yes) or N(no)')

    time.sleep(0.5)
    select = input('>>>')
    if select in ['N','n','no','NO','No']:
        print(f'{name}은 성에서 쫓겨났다.')
        return
    
    elif select in ['Y','YES','Yes','yes','y']:
        print('튼튼한 경제! 하늘을 찌르는 민심을 보여주마!')
        time.sleep(1)
        print('정치가들이 모이기 시작한다.')
        time.sleep(1)
        print(f'{name}: 그래도 독재는 꺠지면 안돼!')

        time.sleep(2)
        print('...')
        time.sleep(1)
        print(f'{name}: 이제 정치하는 법을 알아봐야겠어.')
        time.sleep(1)
        print('정치 방법 : 공탁이 오면 W키를 눌러 지인 사면을, 반란군이 오면 A키를 눌러 병사를 보내고 귀족들이 오면 D키를 눌러 티타임을 가져. 마지막으로 민심이 추락하면 S키를 눌러 금화를 뿌려봐! ')
        time.sleep(1)
        print(f'{name}: 준비됐으면 이제 enter키를 눌러 나랏일을 시작하자!')

        x = input()

        if x == "":
            start2()


    

    

    

