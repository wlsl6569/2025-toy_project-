import json

def load_item():
    with open('character_info', 'r',  encoding='utf-8') as f:
        data = json.load(f)
    return  data ['item']



def add_item(item):
    # 1) UTF-8로 읽기
    with open('character_info', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2) item 수정
    data['item'].append(item)

    # 3) UTF-8로, 한글 그대로 저장
    with open('character_info', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f'"{item}"가 인벤토리에 추가됐다!')

    return data['item']

def use_item():

    with open('character_info', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(data['item'])
    print('어떤 아이템을 사용하시겠습니까?')
    thing = str(input(">>> ").strip())

    if thing not in data['item']:
        print(f'{thing}을 갖고 있지 않다.')
        return data['item']
    
    
    data['item'].remove(thing)

    with open('character_info', 'w', encoding='utf-8' ) as f:
        json.dump(data, f , indent=4, ensure_ascii=False )
    print (f'{thing}을 사용했다!')

    return data['item']




