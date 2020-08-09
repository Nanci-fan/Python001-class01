##创建一个动物的类

class Zoo(object):
    def __init__(self,name):
        self.name=name
        self.animals=[]


    def add_animal(self,animal):
        if type(animal).__name__ in self.animals:
            print(f'{type(animal).__name__} 是存在的')
        else:
            self.animals.append(type(animal).__name__)
            self.__dict__[type(animal).__name__] = animal

#动物类做成静态的参数
class animal(object):

    size={
        '小':1,
        '大':2}

    is_fierce={
        '温顺':False,
        '凶猛':True
    }

    eat_meat={
        '食草':False,
        '食肉':True}

    def __init__(self,size_max,fierce,meat):
        self.size_max = animal.size[size_max]
        self.fierce = animal.is_fierce[fierce]
        self.meat = animal.eat_meat[meat]

        #做判断
        if (self.size_max>=2) and (self.fierce==True) and (self.meat==True):
            print('是凶猛动物')
        else:
            print('是温顺动物')

class Cat(animal):
    def __init__(self,name,size_max,fierce,meat):
        super().__init__(size_max,fierce,meat)
        self.name = name 


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '小', '温顺', '食肉')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')

    print(have_cat)
