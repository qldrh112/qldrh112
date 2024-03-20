# 20240119 
## 01주차 PJT
### 금융상품 데이터 수집

$학습한 내용$
``` python
url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
result = requests.get(url).
return result
```
여기서 url에 json이 들어가 있다고 json 형태로 값을 출력하는 게 아니다. 위 코드를 실행시키면 <Response [200]> 이 출력된다.


$어려웠던 부분$  
problem1 부터 문제를 보자마자 막막했다. 하지만, 수업 시간에 보고 작성한 코드를 기억할 수 있게 천천히 생각하였고, 어느 정도 구색은 갖추게 되었다. 

- 문제1에서 제일 어려웠던 부분은 `  result = XXXX.get(url)` 에 무엇이 들어가야 할 지 모른다는 것이었다. 
- 문제2는 어려운 부분 없이 물 흐르듯이 흘러갔다.
- 문제 3에서 제일 어려웠던 부분은 딕셔너리와 리스트가 복합적으로 결합되어 있을 때, 그것을 추적하는 일이었다.

``` python
for i in wanna_datas:
    for j in i:
      if j == 'fin_prdt_cd':
        new_dict['금융상품코드'] = i[j]
      elif j == 'intr_rate':
        new_dict['저축 금리'] = i[j]
      elif j == 'save_trm':
        new_dict['저축 기간'] = i[j]
      elif j == 'intr_rate_type':
        new_dict['저축금리유형'] = i[j]
      elif j  == 'intr_rate_type_nm':
        new_dict['저축금리유형명'] = i[j]
      elif j == 'intr_rate2':
        new_dict['최고 우대음리'] = i[j]
      new_list.append(new_dict)
  return new_list
```
중간 과정이 생략되었지만, i와 j를 일일이 신경쓰며 작동 과정을 상상하고, 올바른 답을 쓸 수 있도록 해야 한다.

문제 4는 출력 결과가 
``` python
{'저축 금리': 3.5,
            '저축 기간': '6',
            '저축금리유형': 'S',
```
계속 반복되는 골때리는 상황이 생겼다. 이 문제를 해소하는데 약 2시간은 사용한 것 같다. 

``` python
import pprint
import requests

# 상품과 옵션 정보들을 담고 있는 새로운 객체를 만들어 반환하시오.
# [힌트] 상품 리스트와 옵션 리스트를 금융상품 코드를 기준으로 매칭할 수 있습니다.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 변수에 저장합니다.
# 3. 2번의 결과 중 key 값이 "baseList" 인 데이터를 변수에 저장합니다.
# 4. 2번의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 5. 3번에서 저장된 변수를 순회하며, 4번에서 저장된 값들에서 금융 상품 코드가 
#     같은 모든 데이터들을 가져와 새로운 딕셔너리로 저장합니다.
#     저장 시, 명세서에 맞게 출력되도록 저장합니다.
# 6. 5번에서 만든 딕셔너리를 결과 리스트에 추가합니다.


def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "f4f68031cae93b3974bafdb77b3f8a13"

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    result = requests.get(url).json()

  
    rate_dict = {}
    rate_list = []

    output_dict = {}
    output_list = []

    wanna_datas = result['result']
    bwd = wanna_datas['baseList']
    owd = wanna_datas['optionList']

    for i in range(len(bwd)):
        for j in range(len(owd)):
            if bwd[i]['fin_prdt_cd'] == owd[j]['fin_prdt_cd']:
                # True라면 금리 디셔너리에 owd의 정보를 따와라
                rate_dict['저축 금리'] = owd[j]['intr_rate']
                rate_dict['저축 기간'] = owd[j]['save_trm']
                rate_dict['저축 기간'] = owd[j]['intr_rate_type']
                rate_dict['저축금리유형'] = owd[j]['intr_rate_type_nm']
                rate_dict['최고우대금리'] = owd[j]['intr_rate2']

                # 금리 정보를 리스트에 넣어라
                rate_list.append(rate_dict)

                output_dict['금리정보'] = rate_info_list
                # True라면 결과 디셔너리에 bwd의 정보를 따와라
                output_dict['금융상품명'] = bwd[i]['intr_rate']
                output_dict['금융회사명'] = bwd[i]['kor_co_nm']

                # 아웃풋딕셔너리에 3개의 항목을 넣는다.
                output_list.append(output_dict)

    return output_list
                

if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
```

이 문제를 해결하기 위해서 idle 50000줄 정도 돌렸던 것 같다. 각 라인을 프린트하면서 살펴보았음에도 중간 코드에는 이상이 없었던 것으로 추정되고 심지어 `return` 전의 마지막 코드 마저도 잘 동작하였으나 반환된 값을 출력하면 가장 마지막 정보가 계속해서 출력되는 실로 놀라운 일이 발생하였습니다. 여러 가지 자잘한 코드만 수정하려고 하였으나 사실은 거의 전체를 뒤집는 수준으로 수정을 했어야 했었다. 변화를 두려워 해선 안 된다. 답이 안 보인다 싶으면 아쉬워도 다시 공사를 진행해야 할 듯 하다.

$새로 배운 것들$
 - 파이썬에서 서버에 요청을 할 땐 requests를 활용한다는 것
 - 우선 특정 데이터를 뽑아내기 위해선 모든 데이터셋을 확인할 필요가 있다.
 - 리스트가 가장 바깥에 있을 때 append로 하나 씩 추가해보자
 - 딕션너리에 요소를 할당하는 것은 `dict['key'] = 'value'` 뿐만 아니라 get을 통해 가져오는 방법을 이용해 보도록 하자. 코드가 정상적으로 동작할 수 있다.
 - keyError는 키를 딕셔너리에서 키를 참조할 때 해당하는 키가 없다는 것이다.


$느낀 점$
- 첫 단추(1번)을 잘 끼우니 다음 문제는 술술 풀리는 듯한 느낌이 있다.
- 아는 만큼 보인다는 말이 있다. 계속해서 다양한 데이터와 코드를 접해보면서 단박에 이해할 수 있는 역량을 기르는 것이 중요하다고 생각이 든다.
- 혼자서 마지막 문제를 생각하는 데 거의 1시간 30분 이상을 사용했는데 옆 자리에 있던 원빈님께 조언을 구하고 코드를 작성하니 30분 안에 해결하였다. 동료와 함께 열심히 하겠다고 다짐하였지만, 조금밖에 남지 않은 것 같아서 계속 혼자서 생각하려고 한다. PTJ뿐만 아니라 느끼는 것이지만, 가지고 있는 여러 가지 버릇을 발견하곤 한다. 조정 과정을 거치면 곧 해결할 수 있을 것이라고 생각한다.
