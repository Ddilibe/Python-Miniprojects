from error import BaseError
from baser import BaseConvert



class Octadecimal(BaseError, BaseConvert):
    
    def __init__(self,):
        check = False
        while check == False:
            try:
                self.biny = int(input("Input a octadecimal Number: ")) 
                self.biny = Octadecimal.convert_int_to_list(self.biny)
                check = Octadecimal.error_octa(self.biny)
                if check == False:
                    print("Those are not octadecimal numbers")
            except ValueError:
                print("That is not a number at all")
                check = False
        self.option = 10001
        while (check == False) or not(0<self.option<4):
            try:
                self.option = int(input("Input your option: "))
                if (0<self.option<4):
                    check = True
                else:
                    print("Option not in the range")
                    check = False
            except ValueError:
                print("This is not a number at all")
                check = False
        
    def Confirm(self,):
        j = Octadecimal.convert_from_octadecimal_to_denary(self.biny)
        if self.option == 1:
            print("The octadecimal equivalent of ", self.biny,"in denary is",j)
        if self.option == 2:
           j = Octadecimal.convert_from_denary_to_binary(j)
           print("The octadecimal equivalent of",self.biny,"in binary is",j)
        if self.option == 3:
            j = Octadecimal.convert_from_denary_to_hexadecimal(j)
            print("The octadecimal equivalent of",self.biny,"in hexadecimal is",j)
        
    

mon = Octadecimal()
mon.Confirm()

