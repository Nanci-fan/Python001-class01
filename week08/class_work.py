##实现map 的功能，map 就好像是一个迭代器进行运行

# def square(x):
#     return x**2

# m = map(square,range(11))
# print(list(m))

def map_function(x):
    num_list = [i**2 for i in range(x)]
    return num_list


print(map_function(11))