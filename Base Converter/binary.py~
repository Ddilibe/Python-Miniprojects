from error import BaseError
from baser import BaseConvert



class Binary(BaseError, BaseConvert):

    def __init__(self,):
        check = False
        while check == False:
            try:
                self.biny = int(input("Input a Binary Number: ")) 
                self.biny = Binary.convert_int_to_list(self.biny)
                check = Binary.error_binary(self.biny)
                if check == False:
                    print("Those are not binary numbers")
            except ValueError:
                print("That is not a number at all")
                check = False
        self.option = 10010
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

    def confirm(self, ):
        j = Binary.convert_from_binary_to_denary(self.biny)
        if self.option == 1:
            print("The binary equivalent of", self.biny, "in denary is",j)
        if self.option == 2:
            j = Binary.convert_from_denary_to_octadecimal(j)
            print("The binary equivalent of", self.biny, "in octadecimal is",j)
        if self.option == 3:
            j = Binary.convert_from_denary_to_hexadecimal(j)
            print("The binary equivalent of ", self.biny, "in octadecimal is", j)
        
    

mon = Binary()
mon.confirm()
