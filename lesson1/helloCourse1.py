def main():
    name = input("what's your name?")
    hello()
    hello(name)

def hello(to="world"):
    print("hello,",to)

#定义需要执行的函数，这是调用main函数
main()
