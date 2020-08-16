学习笔记
1、完成python的类型的类型划分
变量赋值：
可变数据类型
列表 list 
字典 dict
不可变数据类型
 整型  int 
浮点型 float
元组 tuple
字符串 string


2、变量的赋值可以更具序列的类型分为不同的赋值类型
序列：容器序列和扁平序列，其中容器序列包括 列表，元组，其中可以存放任意的数据类型
扁平序列只能存放一种数据类型
其中容器序列存在深浅拷贝的问题，其中只要是
可以使用import copy 的形式来实现深copy 和浅拷贝的问题
copy_qian = copy.copy(old_list)  #这个是浅copy 不会生成单独的内存
copy_deep = copy.deepcopy(old_list) #这个是深拷贝，会单独占内存，从而当old_list改变了之后copy_deep依然不会变化


二：函数的部分
1、函数的调用问题
函数的调用是不带括号表示调用的是函数的类型而如果是带括号就是调用的函数的值
类似的在python 中一切皆对象的原则，所以类class 也是具有同样的道理

2、变量的作用域
函数的作用域满足LEGB的原则，即L是local，指的是函数内部的调用，
E ：Enclosing function locals 指的是函数嵌套外部的名字空间
G：Global 函数定义所在模块的名字空间
B：Builtin ,python内置模块的命名空间

假设我们定义一个函数
一下就是Local 和Enclosing 的区别
x = 'Global'
def func2():
x = 'Enlocal'
def func3():
x='Local'
print(x)
func3()
print(x)
func2()