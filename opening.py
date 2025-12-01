import time
import json

class_type = ["servant", "farmer", "knight", "loyal", "king"]

def start():

    print("당신은 중세 시대에 떨어졌습니다...")
    time.sleep(1)

    print("주위를 둘러보니 낯선 숲 속입니다.")
    time.sleep(1)

    print("이 곳에서 당신의 이름은 무엇인가요?")
    name = input(">>> ")

    time.sleep(0.5)
    print(f"반갑습니다, {name}님.")

    time.sleep(1)
    print(f"...")

    time.sleep(0.5)
    print(f"{name}님은 이 시대에 어떤 일을 하고 있나요? \n 0 : {class_type[0]} 1 : {class_type[1]} 2 : {class_type[2]}  3 :  {class_type[3]}  4 :{class_type[4]}")

    job = class_type[int(input())]
    time.sleep(1)
    print(f"{name}님... {job}로써 최선을 다해 중세시대를 살아가 주세요...")


    character_info = {
        'name':name,
        'job': job,
        'item':[]
    }

    with open("character_info", 'w') as f :
        json.dump(character_info,f, indent=4)
