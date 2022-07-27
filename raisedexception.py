class InvalidNumber(Exception):
    def __init__(self,arg):
        self.arg=arg
num=int(input())
if(num>10):
    raise InvalidNumber('the number is invalid')
else:
    print(num)
