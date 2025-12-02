import import_character
name, job, item = import_character.load_character()


print(item)

'''
print('농사 방법 : 오전에는 W키를 눌러 광합성을, 
오후에는 A키를 눌러 물을 주고 저녁에는 D키를 눌러 삽으로 땅을 파헤쳐줘. 
마지막으로 삽이 망가지면 S키를 눌러 삽을 수리해봐! ')
'''
time_zone = {'morning': ["W", 'w'],'noon':['A', 'a'],'afternoon':['D', 'd'],'broke':['S', 's']}


def display_timezone():
    if time_zone == 'morning':
        print(f'{name}: 햇빛 무럭무럭 빔~~~~~~.')
    elif time_zone == 'noon':
        print(f'{name}: 시원하게 물을 쫘아아악~~~~~.')
    elif time_zone == 'afternoon':
        print(f'{name}: 흙아 송송 숨을 쉬거라~~~~~.')
    elif time_zone == 'broke':
        print(f'{name}: 뚝딱뚝딱 수리 완료~~~~~.')

round = 5
time_limit = 2

def start2():
    print(f'{name}: 좋아 농사 시작이다! 우하하하하항')

    for i in range(round):
        print(f'============={i+1} / {round}===========')
    