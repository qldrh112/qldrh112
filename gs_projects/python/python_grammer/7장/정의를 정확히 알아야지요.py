from functools import wraps

def test(function):
    @wraps(function)

def wrapper(*arg, **kwargs):
    print("인사가 시작되었습니다.")
    function(*arg, **kwargs)
    print("인사가 종료되었습니다.")
    return wrapper

wrapper(test)
