#!/usr/bin/python3

import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.a, self.b = threading.Event(), threading.Event()
        self.c, self.d = threading.Event, threading.Event
        self.a.set(), self.b.set(), self.c.set(), self.d.set()
        self.h = 1
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(self.h, self.n+1):
            if (i%3==0):
                printFizz()
                self.h = i
            else:
                self.d.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(self.h, self.n+1):
            if (i%5==0):
                printBuzz()
                self.h = i
            else:
                self.c.wait()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(self.h, self.n+1):
            if ((i%3==0)and(i%5==0)):
                printFizzBuzz()
                self.h = i
            else:
                self.b.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.h, self.n+1):
            if ((i%3!=0)and(i%5!=0)):
                printNumber(i)
                self.h = i
            else:
                self.a.wait()

def display(x="thing"):
    print(x)

def num(r):
    print(r)

J = FizzBuzz(13)
J.printFuzz(display)
J.printBuzz(display)
J.printFizzBuzz(display)
J.printNumber(num)
