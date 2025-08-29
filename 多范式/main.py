#################### Python 面向对象编程（OOP），抽象类可借助ABC模块 ####################

# 父类（基类）
class Life:
    def breathing(self):
        print("呼吸")

    def eating(self):
        print("吃饭")


# 父类（基类）
class Animal(object):
    def __init__(self, name):
        # 私有属性，Python 以 __ 标记，用于隐藏内部实现
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # 定义“抽象方法：子类实现处理执行不同的行为，子类需要重写此方法，否则调用会报错
    def speak(self):
        print(f"{self.name} 发出了声音")
        # 多态：不同类的对象，多同一个方法调用可以表现出不同的行为。即“同一个接口，不同的实现”
        # 多态可以通过统一的接口来操作不同的对象，而无需关心对象的具体类型
        raise NotImplementedError("子类必须实现 speak() 方法")


# 类的继承
# 子类（派生类）
class Cat(Animal, Life):
    def speak(self):
        print(f"{self.name} 喵喵喵！")


# 子类（派生类）
class Dog(Animal, Life):
    def speak(self):
        print(f"{self.name} 汪汪汪！")  # 重写父类方法


# 定义通用函数，接收任何 Animal 类型对象
def make_sound(animal: Animal):
    animal.speak()  # 不管传进来的是狗还是猫，只要它有 speak() 方法即可


# 使用
a = Animal("动物")
c = Cat("咪咪")
d = Dog("旺财")

c.speak()  # 咪咪 喵喵喵！
make_sound(c)  # 咪咪 喵喵喵！
c.breathing()  # 呼吸
c.eating()  # 吃饭

d.speak()  # 旺财 汪汪汪！
make_sound(d)  # 旺财 汪汪汪！
c.breathing()  # 呼吸
c.eating()  # 吃饭

print('a is Animal?', isinstance(a, Animal))  # True
print('c is Cat?', isinstance(c, Cat))  # True
print('d is Dog?', isinstance(d, Dog))  # True

print('c is Animal?', isinstance(d, Animal))  # True
print('c is Cat?', isinstance(c, Cat))  # True
print('c is Dog?', isinstance(c, Dog))  # False

print('d is Animal?', isinstance(d, Animal))  # True
print('d is Cat?', isinstance(d, Cat))  # False
print('d is Dog?', isinstance(d, Dog))  # True
