class myComplex:
    def __init__(self, realpart, imgpart):
        self.r = realpart
        self.i = imgpart
        self.number = (self.r, self.i)

    def add(self, num):
        self.r = self.r + num.r
        self.i = self.i + num.i
        self.number = (self.r, self.i)

    def sub(self, num):
        self.r = self.r - num.r
        self.i = self.i - num.i
        self.number = (self.r, self.i)


complex1 = myComplex(2, 1)
complex2 = myComplex(13, 4)
complex1.sub(complex2)

print(complex1.number)
