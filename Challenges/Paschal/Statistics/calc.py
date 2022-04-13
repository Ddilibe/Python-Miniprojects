from state import Calc
from intro import Welcome, Info, EnterInfo, help
import time


mon = Calc("mumu")

def confirm(x):
    if x == "1":
        Enter()
    elif x == "2":
        mon.getCount()
    elif x == "3":
        mon.getSum()
    elif x == "4":
        mon.getMean()
    elif x == "5":
        mon.getStandardDeviation()
    elif x == "6":
        mon.getMax()
    elif x == "7":
        mon.getMin()
    elif x == "8":
        mon.getHelp()
    elif x == "9":
        we = 0
    else: 
        print("Incorrect input")


def check(mon):
    """ Function to check whether the data type is an integer or a float """
    try:
         float(mon)
         return 0
    except (ValueError):
         return 1
         
def Enter():
    """ 
        Function used to pass an argument to the enter method in the Calc class
    """
    EnterInfo()
    dog = input("Input the data: ")
    dump = check(dog)
    if (dump == 0):
        dog = float(dog)
    while (dog != 0):
        dump = check(dog)
        if (dog == 0):
            break
        elif (dump == 0):
            dog = float(dog)
            mon.enter(dog)
            dog = input("Input the data: ")
            dump = check(dog)
            if  (dump == 0):
                dog = float(dog)
        else:
            dog = input("Input the first on was incorrect.\nInput another number: ")
    print("\nData Inputting Complete!!!\n")
    

def start():
    """ 
        This function is used to start the Statistics program.
    """
    Welcome()
    Info()
    help()
    work = input("\n What do you want to do?\n Tape a number lets get started already.\n Number: ")
    while (work != "9"):
        confirm(work)
        if (work != 8):
            work = input("Pls input a number: ")
    print("Thanks for using this program.\nI would really appreciate it if you drop a star for me.")
    
    time.sleep(10)
start()
    
