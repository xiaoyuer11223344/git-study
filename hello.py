# coding=utf-8

from start import start
from end import end

def test():
    start()
    demo()
    print("this is test func")
    end()

def demo():
    print("this is demo func")


if __name__ == '__main__':
    test()
    demo()