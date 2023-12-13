def main():
    x = int(input("what's x ? "))
    #偶数even判断
    if is_even3(x):
        print("Even")
    #奇数odd判断
    else:
        print("odd")

#定义奇偶判断的函数方式一
def is_even1(n):
    if n % 2 ==0:
        return True
    else:
        return False

#定义奇偶判断的函数方式二
def is_even2(n):
    return True if n % 2 == 0  else False 

#定义奇偶判断的函数方式三
def is_even3(n):
    return n % 2 == 0

    
#执行主函数
main()
