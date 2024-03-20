x=input("플레이어의 이름을 설정하여 주십시오")
hp=10 #체력
atc = 10 #공격력
boss_HP = 300 #보스 체력
boss_ATC = 30 #보스 공격력
turn = 0  #후에 5층에서 등장하는 턴
print(x+"님 이시군요 환영합니다.")
print("매 층마다 방을 선택한 후 퀴즈를 맞추면 보상을 얻게 됩니다.")



def print_statement():                   #반복되는 문장 함수로 정의
    print("체력:"+ str(hp))
    print("공격력:"+ str(atc))

    
#1층

y=int(input("방이 2개 있습니다. 1번과 2번 중 선택하여 주십시오."))
print("\n")
while y==1:
    print("빈 방입니다. 절망감으로 체력이 3 감소합니다.")
    hp=hp-3
    print_statement()
    print("\n")
    y=int(input("2번 방을 선택하여 주십시오."))
    print("\n")
if y==2:
    a=input("세상에서 가장 억울한 도형은?")
    if a=="원통":
        if hp<=7:
            print("체력이 20증가합니다.")
            hp=hp+20
            print_statement()
            print("\n")
        else:
            print("체력이 10증가합니다.")
            hp=hp+10
            print_statement()
            print("\n")
            
    else:
        print("문제를 풀지 못해 다음 층으로 이동합니다.")
        print("\n")


#2층
        
z=int(input("방이 2개 있습니다. 1번과 2번 중 선택하여 주십시오"))
while z==1:
    print("낄낄 또 성을 오르는 사람이 왔구만.. 난 상인일세")
    b=input("자네에게 선물을 주지. 의 식 주 중에 뭘 택하겠는가?")
    if b=="의":
        print("갑옷을 얻었습니다. 체력이 증가합니다")
        hp=hp+50
        print_statement()
        print("\n")
        z=int(input("2번 방을 선택해 주십시오."))
        print("\n")
        
    elif b=="식":
        print("장어 덮밥을 얻었습니다.공격력이 10 증가합니다.")
        atc=atc+10
        print_statement()
        print("\n")
        z=int(input("2번 방을 선택해 주십시오."))
        print("\n")

    else:
        print("낄낄..그래 요즘 집값이 올랐지.. 이 물약을 먹게..")
        print("환각에 빠져 성 안에서 살게 됩니다.")
        print("\n")
        z=int(input("다시 하시려면 1을 눌러주세요."))
        print("\n")
        
if z==2:
    c=input("5.18 민주화 운동이 일어난 당시 집권중이던 대통령은?")
    if c=="최규하":
        print("역사의 힘으로 체력과 공격력이 각각 10씩 증가합니다.")
        hp=hp+10
        atc=atc+10
        print_statement()
        print("\n")

    else:
        print("역사의 분노로 체력이 절반이 됩니다.")
        hp=hp/2
        print_statement()
        print("\n")


#3층
        
q=int(input("3층으로 왔습니다. 1번과 2번중 하나를 택해주십시오."))

while q==1:
    d=input("자네는 힘과 건강 무엇을 원하는가?")
    if d=="힘":
        print("체력이 1이 되고 나머지 체력이 공격력이 됩니다.")
        atc=atc+hp-1
        hp=1
        print_statement()
        q=int(input("2번을 눌러주십시오."))
        print("\n")
    else:
        print("공격력이 1이 되고 나머지 공격력이 체력이 됩니다.")
        hp=hp+atc-1
        atc=1
        print_statement()
        print("\n")
        q=int(input("2번을 눌러주십시오."))
        print("\n")

if q==2:
    e=input("이 성을 쌓은자를 아는가? 모른다면 더 이상 게임을 할 필요가 없네. (힌트: 파이썬을 알려준 최고 권위자)")
    if e=="서일정":
        print("기본적인 진리로 보상이 없습니다.다음 층으로 이동합니다.")
        print("\n")

    else:
        print("교수님의 분노로 체력과 공격력이 1이 됩니다.")
        hp=1
        atc=1
        print_statement()
        print("\n")


#4층
        
print("4층 주사위 방입니다. 다음 층은 마지막 층이며 이것이 마지막 시련이자 마지막 기회입니다.")
import random
dice=random.randint(1,6)
w=input("주사위를 굴리시겠습니까?")
print("\n")

if w=="네":
    if dice==1:
        print("1이 나왔습니다. 체력과 공격력이 1이 됩니다.")
        hp=1
        atc=1
        print("현재 체력이"+str(hp)+ "이 되고 공격력이"+str(atc)+ "이 됩니다.")

    elif dice==2:
        print("2가 나왔습니다. 체력과 공격력이 2배가 됩니다.")
        hp=hp*2
        atc=atc*2
        print("현재 체력이"+str(hp)+ "이 되고 공격력이"+str(atc)+ "이 됩니다.")
        
    elif dice==3:
        print("3이 나왔습니다. 체력과 공격력이 1/3배가 됩니다.")
        hp=hp/3
        atc=atc/3
        print("현재 체력이"+str(hp)+ "이 되고 공격력이"+str(atc)+ "이 됩니다.")
        
    elif dice==4:
        print("4가 나왔습니다. 체력과 공격력이 4배가 됩니다.")
        hp=hp*4
        atc=atc*4
        print("현재 체력이"+str(hp)+ "이 되고 공격력이"+str(atc)+ "이 됩니다.")
        
    elif dice==5:
        print("5가 나왔습니다. 체력과 공격력이 1/5배가 됩니다.")
        hp=hp/5
        atc=atc/5
        print("현재 체력이"+str(hp)+ "이 되고 공격력이"+str(atc)+ "이 됩니다.")
        
    else:
        print("6이 나왔습니다. 체력과 공격력이 6배가 됩니다.")
        hp=hp*6
        atc=hp*6
        print("현재 체력이"+str(hp)+ "이 되고 공격력이"+str(atc)+ "이 됩니다.")
else:
    print("도박은 한 가정을 파탄 낼 수 있습니다.(공익광고협의회)")
    print("\n")

    
#5층(보스층)

print("보.스.등.장!!!!!!!")

while  boss_HP >= 0 or hp >= 0:      #보스와 플레이어가 살아있을 때까지 반복
    turn = turn + 1                  #턴 증가
    print_statement()
    print("\n")
    choice = input("공격할 거냐? 체력을 회복할 거냐?")   #플레이어 행동 선택
    if choice == "공격":
        print("에잇~")
        boss_HP = boss_HP - atc
        print("현재 보스의 체력은", boss_HP,"입니다.")     #보스체력 표시
        if boss_HP <= 0:
            print("끼예옉~~ \n 보스를 죽여버렸습니다~~!.")
            print("성오르기 성공!!")
            print("\n")
            print(str(turn),"턴 만에 보스를 물리치셨군요.")
            print("상인:크,,킄",x,"군 정말 축하하네..")        #승리 메시지
            break
    else:
        import random
        heal = random.randrange(30)
        hp = hp + heal                  #랜덤으로 체력 회복
        if heal != 0:
            print("화장실에서 응가를 쌉니다. \n 체력 회복 +",heal)
            print_statement()
        else:
            print("피똥이 나와버렸군요 ^^;;")            #체력 회복량이 0일 시
            print_statement()
    print("\n")
    print(" 보스의 턴입니다.")
    import random                        #보스의 공격 방향 랜덤 선택
    boss_direct = random.randint(1,2)
    direct = int(input("보스의 공격이다!!! \n 몸을 숨길 방향을 선택해라.( 1 = 왼쪽, 2 = 오른쪽)") )
    if  direct == boss_direct:       #피하지 못 함
        print("아야..,♡")
        hp = hp - boss_ATC
        print_statement()
        if hp <= 0:
            print("보스가 당신을 찢어버렸습니다.")       #사망 메시지
            break
        print_statement()
        print("현재 턴 =", turn)
        print("\n")
    else:
        print("회피 갸꿀~")            #회피 성공 
        print_statement()
        print("\n")
        print("현재 턴 =", turn)
        print("\n")
        
    

      

        
