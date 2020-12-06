import json
from bread_factory import BreadFactory
from bread import Bread

json_data = '''[{
    "breadType": "cream",
    "recipe": {
      "flour": 100,
      "water": 100,
      "cream": 200
    }
  },
  {
    "breadType": "sugar",
    "recipe": {
      "flour": 100,
      "water": 50,
      "sugar": 200
    }
  },
  {
    "breadType": "butter",
    "recipe": {
      "flour": 100,
      "water": 100,
      "butter": 50
    }
  }]'''

def main():
    # json을 dict로 변환
    data = json.loads(json_data)

    # Bread 인스턴스를 담을 리스트
    breads = []

    # factory 메서드로 인스턴스 생성
    for chunk in data:
        breads.append(BreadFactory().create_bread(chunk.get('breadType'), chunk.get('recipe')))

    # 출력
    for bread in breads:
        bread.get_info()

main()