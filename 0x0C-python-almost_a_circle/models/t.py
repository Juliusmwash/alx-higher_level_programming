#!/usr/bin/python3

class Testing:
    def __init__(self):
        self.id = 1
        self.__width = 2
        self.__height = 2
        self.__x = 2
        self.__y = 2

    def change_att(self, *args, **kwargs):
        length = len(args)
        for i in range(length):
            if i == 0 and args[i] != None:
                self.id = args[i]
            elif i == 1 and args[i] != None:
                self.__width = args[i]
            elif i == 2 and args[i] != None:
                self.__height = args[i]
            elif i == 3 and args[i] != None:
                self.__x = args[i]
            elif i == 4 and args[i] != None:
                self.__y = args[i]
    def print_data(self):
        print(self.id)
        print(self.__width)
        print(self.__height)
        print(self.__x)
        print(self.__y)

a = Testing()
a.change_att(5, 6, 7, 8, 9)
a.change_att(10, 11)
a.change_att(None, None, None, None, 98)
a.change_att()
a.print_data()

my_dict = {'foo': 'bar', 'baz': 'qux'}

for key, value in my_dict.items():
    if key == 'foo':
        foo_value = value
        break
print("foo_value: {:s}".format(foo_value)) # prints 'bar'
print("my_dict['foo']: {:s}".format(my_dict["foo"]))
print("my_dict.get('foo'): {:s}".format(my_dict.get('foo')))

if "baz" in my_dict:
    print("my_dict.get('baz'): {:s}".format(my_dict.get('baz')))

def my_function(*args, **kwargs):
    print(args)
    print(kwargs)
    if 'foo' in kwargs:
        print("foo present")
        print("kwargs['foo']: {:s}".format(kwargs['foo']))
        string = kwargs['foo']
        print("string: {:s}".format(string))

my_function(1, 2, 3, foo='bar', baz='qux')


# prints (1, 2, 3)
# prints {'foo': 'bar', 'baz': 'qux'}


def func3(*args):
    if args is None:
        print("args is none");
    else:
        print("args is not none")

g = func3(None) # not empty
g = func3(None, 3) # not empty
g = func3() #empty


def my_function(*args):
    print("\n")
    print(len(args))
    if len(args) == 0:
        print('args is empty')
    else:
        for arg in args:
            if type(arg) == list or type(arg) == tuple or type(arg) == dict:
                if len(arg) == 0:
                    print("args is empty")
                else:
                    print("args is not empty") 
            else:
                print("args is not empty")
        #print('args is not empty')

my_function() # prints 'args is empty'
my_function(1, 2, 3) # prints 'args is not empty'
my_function((), [], {}, [3])
my_function(None, None, 56)

var = None
print("\n\ntype var: {}".format(type(var)))

ful =[[]]
if ful:
    print("working")
else:
    print("else called")
