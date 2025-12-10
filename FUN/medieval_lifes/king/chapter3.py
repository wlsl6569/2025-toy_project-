import import_character
from item_add import add_item, use_item
import time, random
import sys


name, job, item = import_character.load_character()

def start3():
    time.sleep(1)
    print(f'...다음 날 아침, {name}은 온 백성 앞에 서있다.')
    time.sleep(1)
    print(f'{name}: 이제 중요한 발표를 하겠습니다.')
    time.sleep(1)
    print('발표식에 착용할 아이템을 고르세요.')

    items, thing = use_item()
    #print("thing: ", thing)
    

    time.sleep(1)
    print(f'{name}은 {thing}를 집어들었다.')
    time.sleep(1)
    print(f'{name}는 어쩐지 가슴이 벅차올랐다.')
    time.sleep(1)
    print(f'{name}: 드디어 이런 순간이 오는구나.')
    time.sleep(1)
    print(f'{name}는 {thing}를 잡아들어 착용한다.')
    time.sleep(1)
    print(f'{name}: 이게 바로 내 힘으로 이뤄낸 세상...')
    time.sleep(1)
    if thing == '왕의 지팡이':
        print(f'{thing}를 들어올리며 세상에 강한 권력만큼 부패하기 쉬운 것은 없으며 \n 자신은 더욱이 욕심을 버리며 백성을 챙기노라 발표한다.')
        print(f'백성들이 모두 환호한다.')
        time.sleep(1)
        print(f'...')
        time.sleep(1)
        print(f'The End')
        return
    elif thing == '황제의 왕관':
        print(f'{thing}을 머리에 착용하며 {name}은 절대권력을 발표한다!')
        time.sleep(1)
        print(f'...')
        time.sleep(1)
        print(f'{name}: 앞으로 나를 똑바로 보는 것도 금지입니다. \n 완벽한 질서는 무력으로만 가능한 것!')
        time.sleep(2)
        print('백성들이 모두 고개를 숙여 존경을 표한다.')
        time.sleep(1)
        print(f'...')
        time.sleep(1)
        print(f'The End')
        return


