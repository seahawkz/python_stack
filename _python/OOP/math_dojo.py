class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
x = md.subtract(x).add(3,2).add(2,5,6,9,1).add(4,5,2,1).result
print(x)
x = md.subtract(x).add(5).add(2,5,3,7,2,4).add(2,1,7,-3,1).result
print(x)

x = md.subtract(x).subtract(2,1,4).subtract(2).subtract(4,1,-29,3).result
print(x)
x = md.subtract(x).subtract(2,3).subtract(4,1,9).subtract(3,1,9,2,1).result
print(x)
x = md.subtract(x).subtract(2,1,4,3).subtract(2,2).subtract(4,1,29).result
print(x)