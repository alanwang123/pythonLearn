# pythonLearn
CS50's Introduction to Programming with Python 
edx上的python课程学习记录。
源代码在每节课程的文件夹内
### lesson1 functions variables
- pseudocode 伪代码
- comma 逗号
- succinct 简洁
- arguments 参数（实参）
- parameters（形参）
- parentheses 括号
- curly braces 大括号
- decimal 小数

**函数定义**
通过def 方法名：
    缩进四个空格或者tab 
>
### lesson2 conditionals 
**链接方式[连接的名称]（括号内的链接的网址）**
[lesson2](https://github.com/alanwang123/pythonLearn/tree/main/lesson2%20conditionals)

- 代码grade.py 描述不同分数的判断输出
- 代码parity.py 奇偶判断函数
**match**用法 参照代码house.py
#match case 相当于Java中的switch case 用 “｜ ”符号表示或者的意思

### lesson3 loops 

- while循环
```python
i = 3
while i != 0:
    print("meow")
    i = i-1
```

- for循环
```python
# range代表一定的范围内
for i in range(3):
    print("meow")
```

-while循环，break 退出
```python
while True:
    n = int(input("what's n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")
```

- 通过主函数实现循环
```python
def main():
    number = get_nember()
    meow(number)


def meow(n):
    for _ in range(n):
        print("meow")
        
def get_nember():
    while True:
            n = int(input("what's n?"))
            if n > 0:
                 break
    return n
main()
```

- 数组循环打印
```python
students = ["alan","peter","lucy"]
for s in students:
    print(s)
```

