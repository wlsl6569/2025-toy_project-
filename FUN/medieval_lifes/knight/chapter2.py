import import_character
from item_add import add_item 
import time, random
from knight.chapter3 import start3

name, job, item = import_character.load_character()


print(item)

'''
훈련 방법 : 오전에는 W키를 눌러 검술 훈련을, 오후에는 A키를 눌러 마을 봉사를 하고 
저녁에는 D키를 눌러 적군을 도발해. 마지막으로 검이 망가지면 S키를 눌러 검을 수리해봐!
'''
time_zone = {'morning': ["W", 'w'],'noon':['A', 'a'],'afternoon':['D', 'd'],'broke':['S', 's']}
item = '명예훈장'

def display_timezone(zone):
    if zone == 'morning':
        print(f'{name}: 아침이 됐다~~~~~~.')
    elif zone == 'noon':
        print(f'{name}: 마을에 갈 시간~~~~~.')
    elif zone == 'afternoon':
        print(f'{name}: 바보같은 적군들이 보여~~~~~.')
    elif zone == 'broke':
        print(f'{name}: 뚝딱뚝딱 수리 완료~~~~~.')

rounds = 5
time_limit = 2

def start2():
    print(f'{name}: 좋아 훈련 시작이다! 우하하하하항')

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
            print('성에서 쫓겨났다!')
            return

        elif key not in time_zone[zone]:
            time.sleep(1)
            print(f'{name}: 으아악 실수 실수')
            time.sleep(1)
            print('성에서 쫓겨났다!')
            return
        
        else:
            time.sleep(1)
            print('기사정신이 올랐다!')


    time.sleep(1)
    print(f"{name}: 우왓~ 기사단장으로 승진~~~~")
    time.sleep(1)
    add_item(item)
    start3()

