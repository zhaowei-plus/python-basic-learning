
############################## 案例：__call__ 调用案例 ######################################
class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self, greeting="Hello"):
        print(f"{greeting}, {self.name}!")

g = Greeter("Alice") ## 调用 __init__，初始化实例属性 nam
g() ## 相当于调用 g.__call__()
g("Hi there") ## 相当于调用 g.__call__("Hi there")

## __call__ 实现计时器类：每次调用增加计数
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        print(f"当前计数: {self.count}")

# 创建计数器对象
counter = Counter()

counter()  # 当前计数: 1
counter()  # 当前计数: 2
counter()  # 当前计数: 3

# __call__: 实现一个“带状态的函数”（类似闭包），如一个累加器
class Adder:
    def __init__(self, initial=0):
        self.total = initial

    # 每次调用内部保存状态，返回计算结果
    def __call__(self, number):
        self.total += number
        return self.total

# 创建一个 Adder，初始值为 10
add = Adder(10)

print(add(5))   # 10 + 5 = 15
print(add(3))   # 15 + 3 = 18
print(add(10))  # 18 + 10 = 28

## 用__call__：实现一个类装饰器
# 实现一个记录函数调用次数的类装饰器
class CalCounter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"函数 {self.func.__name__} 被调用了第 {self.count} 次")
        return self.func(*args, **kwargs)

    def __str__(self):
        """ 被 str() 和 print() 调用时，返回易读字符串 """
        return "DailyMagicMethod string representation"

    def __repr__(self):
        """官方字符串表示，用于调试"""
        return "DailyMagicMethod()"

    def __format__(self, format_spec):
        """被 format() 和 f-string 调用"""
        return f"Formatted: {format_spec}"

# 使用类装饰器
def say_hello():
    print(f"Hello")

say_hello()  # 第 1 次
say_hello()  # 第 2 次
