#!/bin/py Python 3

import math


class Calc():
    """
        This class is a blueprint for the calculation of some basic statistical problems like mean, standard deviation, max input, min input and so on.
    """
    
    total = 0
    
    dataset = []
    
    def __init__(self, tv):
        self.tv = tv
        Calc.total += 1
             
             
    def enter(self, value):
         """ Function that adds the item into the dataset """
         value = float(value)
         Calc.dataset.append(value)
    

    def getMax(self):
        """ Method or functon to get the maximum value in the dataset """
        x = max(Calc.dataset)
        print("The maximum vale in the dataset is ", x, "\n")
        return x 
    

    def getMin(self):
        """ Method or functon to get the minimum value in the dataset """
        x = min(Calc.dataset)
        print("The minimum vale in the dataset is ", x, "\n")
        return x


    def getCount(self):
        """ Function to returns the number of items that have been added to the dataset """
        y = len(Calc.dataset)
        print("The number of items in the dataset is ", y, "\n")
        return y
    

    def getMean(self):
        """ Function that returens the average of all the items in the dataset """
        val = Calc.getSum(self)
        count = Calc.getCount(self)
        me = float(val/count)
        print("Therefore, calculating the mean, we can say that ", end="")
        print("The mean is ", me, "\n")
        return me
        
    
    def getSum(self):
        """ Function to return the sum of all the items that have been added to the dataset """
        x = 0
        y = len(Calc.dataset)
        if y == x:
            print("The dataset is empty")
        else:
            for d in range(0,y):
                x += Calc.dataset[d]
            print("The sum of variable on the dataset is ", x, "\n")
        return x
        
        
    def getStandardDeviation(self):
        mean = Calc.getMean(self)
        count = Calc.getCount(self)
        x = 0
        y = len(Calc.dataset)
        for i in range(0, y):
            x += ((Calc.dataset[i] - mean) * (Calc.dataset[i] - mean))
            print(x)
        answer = x/(count - 1)
        answer = math.sqrt(answer)
        print("The standard Deviation is ", answer, "\n")
    
    
    def __str__(self):
        info = " A blueprint for the calculation of a set of basic statistical functions "
        return info
