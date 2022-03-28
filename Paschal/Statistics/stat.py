class Calc():
    """
        This class is a blueprint for the calculation of some basic statistical problems 
    """

    def __init__(self, param):
         print("Writing into a .txt file")
         text = open("write.txt","a")
         text.close()
         self.param = param
             
    def check(self, mon):
        """ Function to check whether the data type is an integer or a float """
        try:
             float(mon)
             return 0
        except (ValueError):
             print("Please input an integer or a float")
             return 1
             
    def add_known(self, card):
         """ Function that adds the item into the dataset """
         text = open("write.txt", "a")
         value = input("Write the number: ")
         ch = self.check(value)
         while (ch != 0):
                value = input("Write the number: ")
                ch = self.check(value) 
         value = float(value)
         text.writeline(value)
         text.close()
     
    def count(self):
        """ Function to returns the number of items that have been added to the dataset """
        text = open("stat.txt", 'r')
        lines = text.readlines()
        count = 0
        for line in lines:
            count += 1
        text.close()
        return count
         
    def getMean(self):
        """ Function that returens the average of all the items in the dataset """
        val = self.getSum()
        count = self.getCount()
        me = float(val/coun)
        print("The mean is "+ me)
        return me
        
    
    def getSum():
        """ Function to return the sum of all the items that have been added to the dataset """
        text = open("stat.txt", 'r')
        lines = text.readlines()
        sum = 0
        for line in lines:
            line = float(line)
            sum += line
        text.close()
        return sum
        
    def __str__(self):
        info = " A blueprint for the calculation of a set of basic statistical functions "
        return info
        
    
    
    
    
""" 
    Aparently, the above is my first attempt on the problem you gave. So I will be trying to consice it for the time being. Sorry for wasting time. The difference is in the way the datas were saved.  
"""

class Calc():
    """
        This is the second attempt on the method for finding basic statistical values
    """
    total = 0
    dataset = []
    
    @staticmethod
    def getCount():
        return Calc.total
    
    def __init__(self):
        Calc.total += 1