def hello():
    for i in range(10):
        print('hello world!')

def table5():
    for i in range(10):
        print(5 * (i + 1))

def hello2(n, string):
    for i in range(n):
        print(string)

def hello3(array):
    for i in range(len(array)):
        print(array[i] * (i + 1))

hello()
table5()
hello2(3, "hello world")
hello3(["h", "e", "l", "l", "o"])




