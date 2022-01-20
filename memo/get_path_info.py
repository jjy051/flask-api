import os
import sys
import inspect

def first_chapter():
    print("chapter 1: get path info")
    
    # get currnet working directory
    print(os.path)
    print(os.getcwd())
    
    # get file name
    print(__file__)
    
    # get absolute path of this file
    print(os.path.realpath(__file__))
    
    # get absolute parent dircetory of the file
    print(os.path.dirname(os.path.realpath(__file__)))

# first_chapter()

def second_chapter():
    print("chapter 2: get system package path info")

    # get module path for pip installer to looks up
    print(sys.path)
    # get installed modules. 
    # when pip install something, python first sys.modules to check that already installed
    # print(sys.modules)

    # get directory info of a certain package imported
    print(inspect.getfile(os))

second_chapter()


class test_class():
    """ this is a test class"""
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def third_chapter(self):
        print("chapter 2")
        print(self.__dir__)
        print(self.__dir__())
        print(dir(self))
        print(self.__doc__)


obj = test_class()
# obj.third_chapter()


