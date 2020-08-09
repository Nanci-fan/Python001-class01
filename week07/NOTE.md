学习笔记


一 :本文需要解决的三个问题：
1、什么是继承？
类的继承就是在一个类的基础上哟引用另外一个类内容的方法。

2、继承的作用是什么？
继承的作用是方便在代码运行的过程中防止代码的冗余

3、在代码中怎么应用继承，同时怎么样编写继承
首先定义一个类
class BaseClass(object):
def __init__(self,name):
self.name = name

class SubClass(BaseClass):
def __init__(self):
self.age = 18

def Class(self,city,range):
perint(city,range,name)


二 ：用自己的语言复述老师上课的内容

首先说明了object 类和type 类的区别以及继承关系
object 类和type 类都属于type 类
type类是由自身创建的，而object 类是由type类创建的
object 类的父类是空，而type 父类是object 

三：类的继承的分类
单一继承
多重继承
菱形继承
其中菱形的继承的机制是MRO原则

可以理解为 left >right >base 的继承顺序