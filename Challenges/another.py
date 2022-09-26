from threading import Event, Lock
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.a, self.b, self.c, self.d = Lock(), Lock(), Lock(), Lock()
        self.b.acquire(), self.c.acquire(), self.d.acquire()
        self.h = 1
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.b.acquire()
            if self.n == 0:
                return 
            printFizz()
            self.a.acquire()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.c.acquire()
            if self.n == 0:
                return 
            printBuzz() 
            self.a.acquire()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.d.acquire()
            if self.n == 0:
                return 
            printFizzBuzz()
            self.a.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.h, self.n+1):
            self.a.acquire()
            if ((i%3==0)and(i%5==0)):
                self.d.release()
            elif (i%3==0):
                # self.b.acquire()
                self.b.release()
            elif (i%5==0):
                # self.c.acquire()
                self.c.release()
            else:
                printNumber(i)
        self.a.acquire()
        self.n = 0
        self.b.release()
        self.d.release()
        self.c.release()
        return
