class cal:
    def __init__(self, *values):
        self.values = values
        
    def add(self, *values):
        a = 0
        for value in self.values:
            a += value
        return a

    def min(self, *values):
        a = 0
        for value in self.values:
            a -= value
        return a

    def mul(self, *values):
        a = 1
        for value in self.values:
            a *= value
        return a

    def div(self, *values):
        a = 1
        for value in self.values:
            if a == 1:
                a = value
            else:
                a /= value
        return a


