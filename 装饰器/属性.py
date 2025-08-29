import math


# @property： 定义计算属性

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # property: 定义计算属性，方式是直接属性访问，不需要函数调用，如 Circle(3).area
    # TODO：如果仅设置了 property 而未设置 xxx.setter ，那么表示只读
    @property
    def area(self):
        return math.pi * self.radius ** 2

    # 设置 area 属性值
    @area.setter
    def area(self):
        print("设置该属性")
        # TODO: 可以在赋值时验证数据合法性、计算属性值
        self.radius *= 2

    # 删除 area 属性
    @area.deleter
    def area(self):
        print("🗑️ 正在删除 area 属性")
        # del self._name


#### 结合 getter/setter/deleter
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # 内部变量，使用 _ 开头表示“私有”

    # 定义计算属性，隐藏内部实现细节
    @property
    def celsius(self):
        return self._celsius

    # 定义 setter
    @celsius.setter
    def celsius(self, value):
        # 在设置值时，校验参数是否合法
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度！")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * (9 / 5) + 32

# 使用
temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0

temp.celsius = 30
print(temp.fahrenheit)  # 86.0

temp.celsius = -300  # ❌ 报错！ValueError