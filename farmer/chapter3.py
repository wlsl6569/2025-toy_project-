import import_character
from item_add import add_item, use_item
import time, random


name, job, item = import_character.load_character()

def start3():
    time.sleep(1)
    print(f'...고요한 저녁, {name}은 모닥불을 바라보며 앉아있다.')
    time.sleep(1)
    print(f'{name}: 열심히 일했더니 출출하군.')
    time.sleep(1)
    use_item('감자')
    time.sleep(1)
    print('모닥불에 감자를 넣었다.')
    time.sleep(1)
    print(f'{name}는 어쩐지 눈물이 났다.')
    time.sleep(1)
    print(f'{name}: 이건 슬픔의 눈물이 아니야.')
    time.sleep(1)
    print(f'{name}는 뜨거운 감자를 잡아들어 온기를 느낀다.')
    time.sleep(1)
    print(f'{name}: 이게 바로 내 힘으로 이뤄낸 식사구나.')
    time.sleep(1)
    print(f'감자를 먹기 시작한다.')
    time.sleep(1)
    print(f'내일도 또 다른 하루를 기다리게 하는 맛이다.')
    time.sleep(1)
    print(f'...')
    time.sleep(1)
    print(f'The End')

