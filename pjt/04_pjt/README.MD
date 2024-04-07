$ 오늘 계획 $  
09:00 ~ 10:00 : 라이브 강의  
10:00 ~ 11:00 : 라이브 강의  
11:00 ~ 12:00 : pjt-1 준비  
12:00 ~ 13:00 : 점심 식사  
13:00 ~ 14:00 : problem 01
14:00 ~ 15:00 : problem 02
15:00 ~ 16:00 : problem 03
16:00 ~ 17:00 : problem 04
17:00 ~ 18:00 : readme.MD 작성  

$학습한 내용과 새로배운 것$  
### pjt-1 준비
이전에 진행했던 03-pjt의 내용을 활용해 폰트를 먹였다. 
``` html
    {% comment %} cdn {% endcomment %}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">

    {% comment %} google font {% endcomment %}
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic+Coding&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/style.css">
```

그냥 .css를 분리해서 완료되는 것이 아니라 이것도 static 파일이라  pjt-04 경로에 static 파일 경로 설정하고, setting에서 STATICFILES_DIRS 리스트에 BASE_DIRS / 'STATIC' 을 넣어놨다.  
``` python
# settings.py
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```
알다시피 다른 경로로 넣고 싶으면 조정하면 된다.  

이거랑 위에 header 작성하고 나니 11:47이 되었다. 

### problem1
첫번째 문제는 정말 처음 보는 유형이었기에 많은 검색을 요구로 했다.  
처음에는 pyplot에 테이블 형식의 무언가가 있을 것이라 생각해서 그 가능성을 가지고 찾아보았지만 생각보다 잘 풀리지 않았다.  

그래서 AI의 힘을 빌렸는데 pandas에 `to_html`이라는 메서드를 통해 테이블로 변환할 수 있었다.  
css는 다행이도 제공받았기에 코드만 구현하면 되서 다행이었다.  

### problem2
두 번째 문제는 이전에 했던 2번째 pjt에 사용했던 로직을 비슷하게 사용하면 해결할 수 있었다.  
문제가 될 만한 부분은 grid를 표현하는 것이었는데 pyplot에서 메서드를 제공해 주었다.  
그리고 몰랐었는데 웹 페이지를 갱신할 때마다 범례가 중첩되어 이상히 여겨 검색해보았는데  
`plt.clf()`를 사용하면 동작을 멈추었다.  
이 원리에 대해 조금 더 공부해 보아야겠다.

### problem3
3번도 이전에 사용한 `.groupby()`로 해결할 수 있는데, 문제는 처음에 잘 기억이 나지 않았고, 이게 생각보다 어려워서 고전했다. 많은 사람들도 이것에 막혀 어려움을 겪은 것으로 알고 있다.  

무엇보다 고생했던 것은 datetime으로 변환하는 것이 어려웠는데, format 매개변수를 사용하면 인식 형태를 pandas에서 알아서 인식해서 그것을 아는 것이 포인트였다고 생각한다.  

반대로 strftime을 통해 문자열을 datetime으로 바꿀 형식을 지정할 수 있는 것도 아주 중요한 포인트다.  
dtype을 통한 여러 타입 이해와 활용이 이 문제뿐만 아니라 pandas를 사용할 때 아주 중요할 것으로 생각이 든다.  

### problem4
마지막 문제는 분명 코드를 쉽게 만들어주는 방법이 있을 것 같은데 잘 몰라서 그냥 함수를 구현해버렸다.  
index는 따로 참조하는 방법을 몰라 pandas_array 타입이 다루기 어려웠다.  
나는 `unique()` 메서드를 사용해 index 값을 뽑아내고, 그것을 리스트 x에, value_counts()의 값은 리스트 y에 넣어버렸다.  
이후, zip으로 두 리스트를 묶은 뒤, 정렬하기 위해 리스트를 새로 만들어서 값을 분배했다.  

조금 비효율적인 알고리즘을 구현한 것 같은데 그래도 오랜만에 코드 짜는 느낌이 나서 좋았다.  


$어려웠던 부분$  
전체적으로 pyplot 사진으로 만드는 과정에 대해 이해가 부족하니 코드를 보고 작성했던 점이 어려웠었다.  

problem1: csv파일을 그래프로 표현하는 것이 어려웠다.  
problem3: date 형식을 다루는 것이 어려웠다. 특히 type에 대한 이해가 부족해서 원인을 알고도 해결하기 어려웠다.  
problem4: 내림차순으로 정렬하는 것이 어려웠다.  


$느낀 점$  
다행인지 모르겠지만, 17시 55분에 마무리하였다.  
물론, 2개의 버전 모두를 끝내고 싶었지만,
이제는 1가지에 집중할 때가 온 것 같다.  
조금 더 공부하면, 이제 쓸 만한 프로젝트가 나올 것 같다.  