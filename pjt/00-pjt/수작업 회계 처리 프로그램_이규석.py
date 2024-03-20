자산 = ['현금', '매출채권', '재고자산', '소모품', '토지', '건물', '기계장치',
      '차량운반구']
부채 = ['미지급금', '차입금', '선수금']
자본 = ['자본금', '이익잉여금', '주식발행초과금']
수익 = ['매출', '이자수익', '유형자산처분이익']
비용 = ['매출원가', '판매비와관리비',  '급여', '감가상각비', '대손상각비',
      '이자비용', '소모품비', '수수료비용', '연구비']

계정과목 = 자산 + 부채 + 자본 + 수익 + 비용
분개장= [{None:None}]
원장 = dict.fromkeys(계정과목, format(0, ','))

print('-' * 40)
print("기능:\n계정과목확인('계정과목')\n계정과목추가('계정과목')")
print("거래인식()\n원장전기(거래번호)")
print("분개장저장()\n분개장불러오기()\n원장저장()\n원장불러오기()")
print('-' * 40)


def 계정과목확인(ㄱ):
    if ㄱ in 자산 + 부채 + 자본 + 수익 + 비용:
        return '존재합니다.'
    else:
        print(f'사용 중인 계정과목은 \n{자산}')
        print(f'{부채} \n{자본} \n{수익} \n{비용}')
        return '존재하지 않습니다.'


def 계정과목추가(ㄱ):
    if ㄱ not in 계정과목:
        ㄴ = input('계정과목의 유형은? :')
        if ㄴ == '자산':
            자산.append(ㄱ)
            계정과목.append(ㄱ)
            원장[ㄱ] = 0
        elif ㄴ == '부채':
            부채.append(ㄱ)
            계정과목.append(ㄱ)
            원장[ㄱ] = 0
        elif ㄴ == '자본':
            자본.append(ㄱ)
            계정과목.append(ㄱ)
            원장[ㄱ] = 0
        elif ㄴ == '수익':
            수익.append(ㄱ)
            계정과목.append(ㄱ)
            원장[ㄱ] = 0
        elif ㄴ == '비용':
            비용.append(ㄱ)
            계정과목.append(ㄱ)
            원장[ㄱ] = 0
        else:
            return '자산/부채/자본/수익/비용 중 택하시오.'
    else:
        print('이미 등록된 계정과목입니다. \n다른 계정과목을 등록하시오.')
        ㄷ = input('계정과목의 명칭은? :')
        계정과목추가(ㄷ)

        
def 거래인식():
    import datetime 
    print('날짜 양식 yyyy-mm-dd')
    거래일 = input('거래 일시: ')
    일시 = datetime.datetime.strptime(거래일 , '%Y-%m-%d')

    
    차변계정 = input('차변의 계정과목: ').split()
    차변액 = []
    대변계정 = input('대변의 계정과목: ').split()
    대변액 = []

    
    for i in 차변계정:
        if i not in 자산 + 부채 + 자본 + 수익 + 비용:
            print('차변의 계정과목이 존재하지 않습니다.')
            거래인식()
        else:
            x = int(input(f'{i} 금액: '))
            차변액.append(x)
    for j in 대변계정:
        if j not in 자산 + 부채 + 자본 + 수익 + 비용:
            print('대변의 계정과목이 존재하지 않습니다.')
            거래인식()
        else:
            y = int(input(f'{j} 금액: '))
            대변액.append(y)
            
    차변합 = 0
    차변 ={}
    대변합 = 0
    대변 ={}
    
    for i in 차변액:
        차변합 += i
    for j in 대변액:
        대변합 += j
    if 차변합 != 대변합:
        print('대차 금액이 일치하지 않습니다.')
        거래인식()
        
    for i in range(len(차변계정)):
        차변[차변계정[i]] = format(차변액[i], ',')
    for j in range(len(대변계정)):
        대변[대변계정[j]] = format(대변액[j], ',')
        
    적요 = input('적요: ')

    print(일시.year,일시.month,일시.day, end='')
    print('{0:>50}'.format(적요))
    
    print(f'(차){[차변]}         (대){[대변]}')
    응답 = input('입력 결과가 맞습니까? ㅇ/ㄴ ')
    if 응답 == 'ㅇ':
        분개 = {'(거래번호)' :len(분개장), '(일시)' :거래일, '(차변)' :차변, '(대변)' :대변, '(거래 내용)' :적요}
        분개장.append(분개)
    else:
        거래인식()

        
def 원장전기(ㄱ):
    a = []
    if ㄱ < len(분개장):
        x = 분개장[ㄱ]
        for i in x.values():
            a.append(i)  
        b = a[2]      #[현금:0]
        c = list(b)     #['현금']
        d = b.get(c[0]) #'10,000'
        e = a[3]      #[차입금:0]
        f = list(e)     #['차입금']  
        g = e.get(f[0]) #'10,000'
        
        차변기초 = int(원장.pop(c[0]))
        if c[0] in 자산 + 비용:
            원장.setdefault(c[0], 차변기초 + int(d.replace(',','')))
        else:
            if 차변기초 >= int(d.replace(',','')):
                원장.setdefault(c[0], 차변기초 - int(d.replace(',','')))
            else:
                print(f'원장 계정 음수: 거래번호{ㄱ} 다시 확인해볼 것')
                
        대변기초 = int(원장.pop(f[0]))
        if f[0] in 부채 + 자본 + 수익: 
            원장.setdefault(f[0], 대변기초 + int(g.replace(',','')))
        else:
            if 대변기초 >= int(g.replace(',','')):
                원장.setdefault(f[0], 대변기초 - int(g.replace(',','')))
            else:
                if 차변기초 >= int(g.replace(',','')):
                    print(f'원장 계정 음수: 거래번호{ㄱ} 다시 확인해볼 것')
    else:
        print(f'거래번호{ㄱ}은 존재하지 않음.')
                      

def 분개장저장():
    import pickle
    f = open('분개장.txt', 'wb')
    pickle.dump(분개장, f)
    f.close()
    return '저장 완료.'

def 원장저장():
    import pickle
    f = open('원장.txt', 'wb')
    pickle.dump(원장, f)
    f.close()
    return '저장 완료.'

def 분개장불러오기():
    global 분개장
    import pickle
    f = open('분개장.txt', 'rb')
    data = pickle.load(f)
    분개장 = data
    return data

def 원장불러오기():
    global 원장
    import pickle
    f = open('원장.txt', 'rb')
    data = pickle.load(f)
    원장 = data
    return data
