print("hello")

# shallo copy
# creates a copy of the object but references each element of the object
# acts differently in nested list

# deep copy
# creates a copy of the object and the elements of the object.


import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
#new_list = copy.deepcopy(old_list)

new_list[0][2] = 'c'

print(old_list)
print(new_list)

# shallow copy, deep copy no diff in below case
list1 = [1,2,3,4]
list2 = copy.copy(list1)
#list2 = copy.deepcopy(list1)
list2[2] = 'c'
print(list1)
print(list2)


'''
Iterator protocol __iter__ and __next__

'''
my_lsit = [1,2,3,4]
print(my_lsit)
my_iter = iter(my_lsit)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

'''
Generators
simple way of creating iterators
function with yield instead of return
local variables of the function shall be remembered for each yield.
call returns to the caller on yield.
generators are good memory saver than list comprehension , diff is instead of [] , generators use ()
 Easy to implement
 memory efficient
 infinite stream
 pipelining generators
'''

my_lsit = [1,2,3,4]

compre = [x**2 for x in my_lsit]

print(compre)

gener = (x**2 for x in my_lsit)

print(next(gener))
print(next(gener))
print(next(gener))
print(next(gener))
#print(next(gener))


'''
Closure
provides some kind of data hiding.
Closures can avoid the use of global values and provides some form of data hiding
'''

print("closure")
def make_multi(n):
    def multi(x):
        return x * n
    return multi

times3 = make_multi(3)
times5 = make_multi(5)

print(times3(9))
print(times5(3))

print(times3(times5(2)))


''' Decorators
add functionality to existing program
at compile time , it is called metaprogramming
 
'''

import datetime

dt_obj = datetime.datetime.now()
print(dt_obj)

dt_obj = datetime.date.today()
print(dt_obj)

# get all attributes of the module
print(dir(datetime))

# date, time , datetime, timedelta



import configparser

config = configparser.RawConfigParser()
config.read(filename)








