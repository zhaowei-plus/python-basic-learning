# 异常处理

## 异常捕获

try...except来捕获并处理这些异常，防止程序崩溃

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ 不能除以零！")
```

## 内置异常类
### Exception
### ArithmeticError
### ZeroDivisionError
### TypeError
### ValueError
### IndexError
### KeyError
### AttributeError
### NotImplementedError
### FileNotFoundError


## 自定义异常

### HTTPException