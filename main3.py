class Bob:
    def __init__(self, num1):
        self.num1 = num1

    def salary(self):
        return self.num1 * 0.25

class Tom:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
  
    def salary(self):
        return self.num1 * 0.25 + self.num2

job = [
    Bob(5),
    Tom(3,4)
]

for i in job:
    print(i.salary())

