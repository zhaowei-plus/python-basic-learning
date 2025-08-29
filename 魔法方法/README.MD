
# Python 魔法方法

## 对象生命周期

### _init__(self, ...) 

> 构造函数，对象创建时初始化属性

### __new__(cls, ...)

### __del__(self)


## 对象的字符串表示

### __str__(self)
### __repr__(self)

## 运算符重载（让对象支持 +、-、== 等操作）

### __add__(self, other)
### __sub__(self, other)
### __eq__(self, other)
### __lt__(self, other)
### __format__(self, other)
### __hash__(self)

## 容器行为（让对象像列表、字典）

### __len__(self)
### __getitem__(self, key)
### __setitem__(self, key, value)
### __delitem__(self, key)
### __contains__(self, item)

## 对象像函数一样被调用

### __call__(self, ...)

## 上下文管理（支持 with语句）

### __enter__(self)
### __exit__(self, exc_type, exc_val, exc_tb)

## 属性访问控制

### __getattr__(self, name)
### __setattr__(self, name, value)
### __delattr__(self, name)

