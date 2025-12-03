import import_character
from item_add import add_item 
import time, random
from loyal.chapter3 import start3

name, job, item = import_character.load_character()


print(item)

'''
 print('놀이 방법 : 오전에는 W키를 눌러 보석을 사들여. 
 오후에는 A키를 눌러 폭식을 하고 저녁에는 D키를 눌러 술을 마셔. 
 마지막으로 자괴감이 올라오면 S키를 눌러 기부를 해봐! ')
        
'''
time_zone = {'morning': ["W", 'w'],'noon':['A', 'a'],'afternoon':['D', 'd'],'broke':['S', 's']}
item = '우울증'

def display_timezone(zone):
    if zone == 'morning':
        print(f'{name}: 보석이 반짝반짝~~~~~~.')
    elif zone == 'noon':
        print(f'{name}: 양고기, 포도, 연어 모두 맛있다~~~~~.')
    elif zone == 'afternoon':
        print(f'{name}: 와인을 더 내놓거라~~~~~.')
    elif zone == 'broke':
        print(f'{name}: 흐흑, 나도 좋은 사람이지?')

rounds = 5
time_limit = 2

def start2():
    print(f'{name}: 좋아 귀족의 일상 시작이다! 우하하하하항')

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
            print('흥이 죽어버렸다!')
            return

        elif key not in time_zone[zone]:
            time.sleep(1)
            print(f'{name}: 으아악 실수 실수')
            time.sleep(1)
            print('흥이 죽어버렸다!')
            return
        
        else:
            time.sleep(1)
            print('흥이 난다!')


    time.sleep(1)
    print(f"{name}: 우왓~ 인생은 즐거워~~~~")
    time.sleep(1)
    add_item(item)
    start3()

