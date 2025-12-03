import import_character
from item_add import add_item 
import time, random
from farmer.chapter3 import start3

name, job, item = import_character.load_character()


print(item)

'''
print('농사 방법 : 오전에는 W키를 눌러 광합성을, 
오후에는 A키를 눌러 물을 주고 저녁에는 D키를 눌러 삽으로 땅을 파헤쳐줘. 
마지막으로 삽이 망가지면 S키를 눌러 삽을 수리해봐! ')
'''
time_zone = {'morning': ["W", 'w'],'noon':['A', 'a'],'afternoon':['D', 'd'],'broke':['S', 's']}
item = '감자'

def display_timezone(zone):
    if zone == 'morning':
        print(f'{name}: 햇빛 무럭무럭 빔~~~~~~.')
    elif zone == 'noon':
        print(f'{name}: 시원하게 물을 쫘아아악~~~~~.')
    elif zone == 'afternoon':
        print(f'{name}: 흙아 송송 숨을 쉬거라~~~~~.')
    elif zone == 'broke':
        print(f'{name}: 뚝딱뚝딱 수리 완료~~~~~.')

rounds = 5
time_limit = 2

def start2():
    print(f'{name}: 좋아 농사 시작이다! 우하하하하항')

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
            print(f'{name}:....너무 늦었어.')
            time.sleep(1)
            print('감자가 시들어버렸다!')
            return

        elif key not in time_zone[zone]:
            time.sleep(1)
            print(f'{name}: 으아악 실수 실수')
            time.sleep(1)
            print('감자가 시들어버렸다!')
            return
        
        else:
            time.sleep(1)
            print('감자가 자랐다!')


    time.sleep(1)
    print(f"{name}: 우왓~ 감자 풍년~~~~")
    time.sleep(1)
    add_item(item)
    start3()

