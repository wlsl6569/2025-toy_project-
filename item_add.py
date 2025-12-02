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




