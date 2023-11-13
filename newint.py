class Newint(int):
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        if self.x == other == 2:
            return 5
        else:
            return self.x + other
newint = Newint(3)
print(newint + 3)

