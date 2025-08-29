
class Person:
    species = "Person"  # 类变量

    def __init__(self, species):
        self.species = species  # 实例变量


    # classmethod 用于定义一个属于类本身而不是类实例的方法, 类方法既可以通过类调用，也可以通过实例调用​​
    @classmethod
    def get_species(cls):
        # cls 代表类本身，通常是 Person
        # 可以访问或修改类属性
        print(cls.species) # 类方法：只能访问类变量
        return cls.species

    @classmethod
    def create_default_person(cls):
        # 类方法作为“工厂方法”，返回一个默认的 Person 字段
        return cls(f"Default {cls.__name__}") # cls 相当于 Person

Person.get_species() # 类调用：-> Person
person = Person("Alice")
person.get_species() # 类实例调用： -> Alice
Person.create_default_person().get_species() # 作为工厂函数返回新实例调用：-> Default Person



##################### 类方法案例1: 类方法作为工厂方法，用于替代构造函数 #############################


# 当希望提供多种方式创建一个对象时，可以使用类方法
class Date:
    # 使用构造函数创建方法
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_str):
        year, moth, day = map(int, date_str.split("-"))
        return cls(year, moth, day)  #调用真正的构造函数


############################## 类方法案例2：获取请求地址 ######################################

class Host:
    def __init__(self, protocol, ip, port):
        self.protocol = protocol
        self.ip = ip
        self.port = port

    # 根据域名组装Host地址
    @classmethod
    def from_domain(cls, protocol, domain, port):
        return cls(protocol, domain, port)

    # 从北极星解析Host地址
    @classmethod
    def from_polaris(cls, protocol, env, address):
        return cls(protocol, env, address)

    # 魔术方法：生成请求地址
    def __str__(self):
        return f"{self.protocol}://{self.ip}:{self.port}"

    # 魔术方法：生成请求地址
    def __repr__(self):
        return f"{self.protocol}://{self.ip}:{self.port}"

    # 当一个类实现了 __call__ 方法，该类就可以想一个方法来调用了
    def __call__(self, *args, **kwargs):
        print(f"对象被调用了！参数: args={args}, kwargs={kwargs}")
        # 后面执行业务逻辑


############################## 类方法案例3：统计实例数量 ######################################

class Car:
    count = 0 # 类变量，用于记录创建了多少个 Car 实例
    countMap = {}  # 实例Map，保存实例列表
    def __init__(self, name):
        self.name = name # 实例变量，类方法无法访问
        Car.count += 1  # 每次创建实例时，类变量数量 +1
        Car.countMap[name] = self # 保存实例

    # 获取实例数量
    @classmethod
    def get_total_cars(cls):
        return cls.count

    # 获取实例对象
    @classmethod
    def get_instance(cls, name):
        return cls.countMap[name]


# 创建几个 Car 实例
car1 = Car("Tesla")
car2 = Car("BMW")
car3 = Car("Toyota")

# 通过类方法获取总数
print("Car:", Car.get_total_cars())  # 输出: 3
print("Car:", Car.get_instance("BMW").name)  # 输出: BMW
