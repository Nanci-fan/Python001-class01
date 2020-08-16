##作业一：
"""
容器序列：list、tuple、dict、collections.deque
扁平序列：str
"""

#作业二
##实现map 的功能，map 就好像是一个迭代器进行运行

# def square(x):
#     return x**2

# m = map(square,range(11))
# print(list(m))

def map_function(x):
    num_list = [i**2 for i in range(x)]
    return num_list


print(map_function(11))


#作业三
import time
def timer(func,*args,**kwargs):
    def package(*args,**kwargs):
        starttime = time.time()
        func(*args,**kwargs)
        endtime = time.time()
        runtime = endtime - starttime
        print(f'运行的时间是: {runtime}')
    
    
    return package

@timer
def test(s):
    time.sleep(s)

test(2)

