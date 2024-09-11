class Mathematics:
    def __init__(self):
        self.a = 14
        self.b = 25
    def sum(self):
        print(f"Sum is: {self.a + self.b}")
    def __sum(self):
        print(f"This is private sum: {self.a + self.b}")
    def _sum(self):
        print(f"This is protected sum: {self.a + self.b}")


obj = Mathematics()
obj.sum()
obj.__sum()
obj._sum()