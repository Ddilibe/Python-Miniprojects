import multiprocessing
import time
import random
import sys
#
# Functions used by test code
#
def calculate(func, args):
    result = func(*args)
    return '%s says that %s%s = %s' % (
            multiprocessing.current_process().name,
            func.__name__, args, result
            )

def calculatestar(args):
    return calculate(*args)

def mul(a, b):
    time.sleep(0.5*random.random())
    return (a*b)

def plus(a, b):
    time.sleep(1*random.random())

f = lambda x : 1/(x-5)
pow3 = lambda x: x**3
def noop(x):
    pass

def test():
    PROCESSES = 4
    print(f"Creating pool with {PROCESSES} processes\n")

    with multiprocessing.Pool(PROCESSES) as pool:
        TASKS = [(mul, (i, 7)) for i in range(10)] + \
                [(plus, (i, 8)) for i in range(10)]
        results = [pool.apply_async(calculate, t) for t in TASKS]
        imap_it = pool.imap(calculatestar, TASKS)
        imap_unordered_it = pool.imap_unordered(calculatestar, TASKS)

        print('Ordered results using pool.apply_async():')
        for r in results:
            print("\t", r.get())
        print()

        print("Ordered results usnig pol.imap():")
        for i in imap_it:
            print('\t', i)
        print()
        
        print("Unordered results using pool.imap_unordered():")
        for x in imap_unordered_it:
            print("\t", x)
        print()

        print("Ordered results using pool.map() --- will block till complete:")
        for x in pool.map(calculatestar, TASKS):
            print("\t", x)
        print()
        
        #
        # Test error handling
        #

        print('Testing error handling:')

        try:
            print(pool.apply(f, (5,)))
        except ZeroDivisionError:
            print("\tGot ZeroDivisionError as expexted from pool.apply()")
        else:
            raise AssertionError("excected ZeroDivisionError")

        try:
            print(pool.map(f, list(range(10))))
        except ZeroDividionError:
            print("\tGot ZeroDivisionError as expexted from pool.map()")
        else:
            raise AssertionError("expected ZeroDivisionError")

        try:
            print(list(pool.imap(f, list(range(10)))))
        except ZeroDivisionError:
            print("\tGot ZeroDivisionError as expected from list(pool.imap())")
        else:
            raise AssertionError('expected ZeroDivisionError')

        it = pool.imap(f, list(range(10)))
        for i in range(10):
            try:
                x = next(it)
            except ZeroDivisionError:
                if i == 5:
                    pass
            except StopIteration:
                break
            else:
                if i == 5:
                    raise AssertionError('expected ZeroDivisionError')

        assert i == 9
        print('\tGot ZeroDivisionError as expected from IMapIterator.next()')
        print()

        #
        # Testing timeouts
        #

        print('Testing ApplyResult.get() with timeout:', end=' ')
        res = pool.apply_async(calculate, TASKS[0])
        while 1:
            sys.stdout.flush()
            try:
                sys.stdout.write(f'\n\t{res.get(0.02)}')
                break
            except multiprocessing.TimeoutError:
                sys.stdout.write('.')
        print('\n\nTesting IMapIterator.next() with timeout:', end=" ")
        it = pool.imap(calculatestar, TASKS)
        while 1:
            sys.stdout.flush()
            try:
                sys.stdout.write(f'\n\t{it.next(0.02)}')
            except StopIteration:
                break
            except multiprocessing.TimeoutError:
                sys.stdout.write('.')
        print("\n\n")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    test()
