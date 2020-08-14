class Person :
    '这是一个学习Python定义的一个Person类'
    # 下面定义了一个类变量
    hair = 'black'
    hat = 'red'
    def __init__(self, name = 'Charlie', age=8,tall=160,weight=53):
        # 下面为Person对象增加2个实例变量
        self.name = name
        self.age = age
        self.tall = tall
        self.weight = weight
    # 下面定义了一个say方法
    def say(self, content):
        print(content)
        print(self.name)
        print(self.age)
        print(self.tall)
        print(self.weight)
        print(self.hat)
        print(self.eye)
        
    def set_hat(self,collor):
        self.hat = collor

    def eye(self, x):
        self.eye = x




p = Person("yicheng",14,160,53)
p.set_hat("blue")
p.eye(5.3)
p.say("123")



