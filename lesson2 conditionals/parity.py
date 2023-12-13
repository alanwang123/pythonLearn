def main():
    x = int(input("what's x ? "))
    #偶数even判断
    if is_even(x):
        print("Even")
    #奇数odd判断
    else:
        print("odd")

#定义奇偶判断的函数
def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False
    
#执行主函数
main()
