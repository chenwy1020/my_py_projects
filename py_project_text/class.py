class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我是 %s ,体重为 %.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("我是 %s ，我爱跑步" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("我是 %s , 我是吃货" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75)

print(xiaoming)

xiaoming.eat()
xiaoming.run()

print(xiaoming)

xiaomei = Person("小美", 45)
print(xiaomei)

xiaomei.eat()
xiaomei.run()

print(xiaomei)


