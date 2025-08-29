## 方法



### Lambda

> Lambda 函数是 Python 中的匿名（没有名字的）小函数，使用关键字 lambda定义，通常用于需要“简单函数”的场合，比如作为参数传给高阶函数（如 map()、filter()、sorted()等）。


```python
# 示例 1：用 map()对列表每个元素做操作
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # 输出 [1, 4, 9, 16]


# 示例 2：用 filter()过滤列表中的偶数
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # 输出 [2, 4, 6]


# 示例 3：用 sorted()按某个规则排序
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

# 按 age 从小到大排序
sorted_people = sorted(people, key=lambda p: p["age"])
print(sorted_people)
# 输出：[{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]
```







