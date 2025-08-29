# Python 现有工具库已实现深/浅拷贝
import copy

a = [1, 2, [3, 4]]
c = copy.copy(a)  # 浅拷贝
b = copy.deepcopy(a)  # 深拷贝

b[2][0] = 999
c[2][0] = 666
print(a)  # [1, 2, [3, 4]]    ← 原对象不变
print(b)  # [1, 2, [999, 4]]  ← 副本变了
print(c)  # [1, 2, [999, 4]]  ← 副本变了


# 自定义实现深拷贝
# 流程：
# 1、判断对象类型
# - 不可变数据类型（如int、str、tuple等），直接返回（不需要拷贝）
# - 可变数据类型（如list、dict、set等）递归创建新对象并复制内容
# 2、对自定义类的对象，也要递归拷贝其属性

def selfDeepcopy(obj, memo=None):
    if memo is None:
        memo = {}

    # 如果是不可变类型, 则直接返回
    if isinstance(obj, (int, float, str, bool, type(None))):
        return obj

    # 防止循环引用
    # id(obj) 是 python 内置方法，用于获取obj内存地址
    print("id:", id(obj))
    if id(obj) in memo:
        return memo[id(obj)]

    # 处理list
    if isinstance(obj, list):
        new_list = []
        memo[id(list)] = new_list  # 先记录，防止循环引用
        for item in obj:
            new_list.append(selfDeepcopy(item, memo))
        return new_list

    # 处理dict
    elif isinstance(obj, dict):
        new_dict = {}
        memo[id(dict)] = new_dict  # 先记录，防止循环引用
        for key, value in obj.items():
            new_dict[selfDeepcopy(key, memo)] = selfDeepcopy(value, memo)
        return new_dict

    # 处理set
    elif isinstance(obj, set):
        new_set = set()
        memo[id(obj)] = new_set  # 先记录，防止循环引用
        for item in obj:
            new_set.add(selfDeepcopy(item, memo))
        return new_set

    else:
        # 其他情况（例如自定义独享）， 默认返回原对象【TODO：这里根据实际情况做额外处理】
        return obj

a = [1, 2, [3, 4]]
b = selfDeepcopy(a)
b[2][0] = 999

print(a)  # [1, 2, [3, 4]]
print(b)  # [1, 2, [999, 4]]