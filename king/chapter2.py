import import_character
from item_add import add_item 
import time, random
from king.chapter3 import start3

name, job, item = import_character.load_character()


print(item)

'''
'정치 방법 : 공탁이 오면 W키를 눌러 지인 사면을, 반란군이 오면 A키를 눌러 병사를 보내고 귀족들이 오면 D키를 눌러 티타임을 가져.
 마지막으로 민심이 추락하면 S키를 눌러 금화를 뿌려봐! '
'''
time_zone = {'morning': ["W", 'w'],'noon':['A', 'a'],'afternoon':['D', 'd'],'broke':['S', 's']}
item = '황제의 왕관'

def display_timezone(zone):
    if zone == 'morning':
        print(f'{name}: 친구가 귀한 선물을 보냈네~~~~~~.')
    elif zone == 'noon':
        print(f'{name}: 반란군을 모두 쓸어버려라~~~~.')
    elif zone == 'afternoon':
        print(f'{name}: 손님들께 차를 내오거라~~~~~.')
    elif zone == 'broke':
        print(f'{name}: 백성 여러분, 금화를 받으세요~~~~~.')

rounds = 5
time_limit = 2

def start2():
    print(f'{name}: 좋아 정치 입문이다! 우하하하하항')

    for i in range(rounds):
        print(f'============={i+1} / {rounds}===========')
        zone = random.choice(list(time_zone.keys()))
        display_timezone(zone)
        
        start = time.time()
        key = input('>>> ').strip()
        end = time.time()
        duration = end - start

        if duration > time_limit:
            time.sleep(1)
            print(f'{name}:....대응이 늦었어.')
            time.sleep(1)
            print('왕권이 약해지며 민주주의가 되었다!')
            time.sleep(1)
            print('{name}은 설 자리를 잃었다..')
            return

        elif key not in time_zone[zone]:
            time.sleep(1)
            print(f'{name}: 으아악 실수 실수')
            time.sleep(1)
            print('왕권이 약해지며 민주주의가 되었다!')
            time.sleep(1)
            print('{name}은 설 자리를 잃었다..')
            return
        
        else:
            time.sleep(1)
            print('왕권은 굳건하다!')


    time.sleep(1)
    print(f"{name}: 우왓~ 왕은 영원하다~~~~")
    time.sleep(1)
    add_item(item)
    start3()

