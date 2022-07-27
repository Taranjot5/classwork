class demo:
    _a=47
class b(demo):
    def __init__(self):
        super().__init__()
        

        print(self._a)
obj=b()
