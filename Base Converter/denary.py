from error import BaseError
from baser import BaseConvert

class Denary(BaseError, BaseConvert):

    def __init__(self, ):
        check = False
        while check == False:
            try: 
                self.biny = int(input("Input a denary Number: "))
                biny = Denary.convert_int_to_list(self.biny)
                check = Denary.error_denary(biny)
                if check == False:
                    print("Those are not denary numbers")
            except ValueError:
                print("That is not a number at all")
                check = False
        self.option = 1432
        while (check == False) or not(0 < self.option < 4):
            try:
                self.option = int(input("Input Your option: "))
                if (0 < self.option < 4):
                    check = True
                else: 
                    print("Option not in range")
                    check = False
            except ValueError:
                print("This is not a number at all")
                check = False

    def confirm(self, ):
        if self.option == 1:
            j = Denary.convert_from_denary_to_binary(self.biny)
            print("The denary equivalent of",self.biny,"in  binary is",j)
        if self.option == 2:
            j = Denary.convert_from_denary_to_octadecimal(self.biny)
            print("The denary equivalent of",self.biny,"in octadecimal is",j)
        if self.option == 3:
            j = Denary.convert_from_denary_to_hexadecimal(self.biny)
            print(f"The denary equivalent of {self.biny} in hexadecimal is {j}")

mon = Denary()
mon.confirm()
