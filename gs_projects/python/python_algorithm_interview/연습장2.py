# 요구 사항 1 이름을 인자로 받아서 생성
# 요구 사항 2 인스턴스가 만들어질 때마다 카운트가 하나씩 증가

class Account:
    total_account = 0

    def __init__(self, name):
        self.name = name
        Account.total_account += 1
        print(f'{self.name}님의 계좌가 생성되었습니다.')

    @staticmethod
    def show_total_account():
        return f'계좌를 생성한 사람의 수: {Account.total_account}'


p1 = Account('이규석')
print(Account.show_total_account())
print()

p2 = Account('김갑돌')
print(Account.show_total_account())
print()

p3 = Account('나도경')
print(Account.show_total_account())
print()

