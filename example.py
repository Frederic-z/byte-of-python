#coding=utf-8
#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
nums = [1, 2, 3]
# print calc(*nums)
#关键字参数
'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Micheal', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
#简化写法

extra = {'city': 'Beijing', 'job': 'Enginner'}
person('Jack', 24, **extra)
'''
#命名关键字参数
'''
def person(name, age, **kw):
    if 'city' in kw:
        #有city参数
        pass
    if 'job' in kw:
        #有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('Jack', 24, 'Beijing', 'Engineer')

def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer')
'''

#参数组合

def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
'''
f1(1, 2)
#a= 1 b= 2 c= 0 args= () kw= {}
f1(1, 2, c=3)
#a= 1 b= 2 c= 3 args= () kw= {}
f1(1, 2, 3, 'a', 'b')
a= 1 b= 2 c= 3 args= ('a', 'b') kw= {}
f1(1, 2, 3, 'a', 'b', x=99)
a= 1 b= 2 c= 3 args= ('a', 'b') kw= {'x': 99}
f2(1, 2, d=99, ext=None)
a= 1 b= 2 c= 0 d= 99 kw= {'ext': None}
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
'''
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)




''' '''