from Formular.error import BaseError
from Formular.baser import BaseConvert

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


class Hexadecimal(BaseConvert, BaseError):

    def __init__(self, ):
        check = False
        while check == False:
            self.biny = str(input("Input the hexadecimal number: "))
            check = Hexadecimal.error_hexa(self.biny)
        check = False
        while check == False:
            try:
                self.option = int(input("Input your option: "))
                if (0 < self.option < 4):
                    check = True
                else:
                    print("Option not in range")
                    check = False
            except ValueError:
                print("That is not a number at all")
                check = False

    def confirm(self,):
        j = Hexadecimal.convert_from_hexadecimal_to_denary(self.biny)
        if self.option == 1:
            print("The hexadecimal equivalent of ", self.biny," in denary is ", j)
        if self.option == 2:
            j = Hexadecimal.convert_from_denary_to_binary(j)
            print("The hexadecimal equivalent of ", self.biny,"in binary is",j)
        if self.option == 3:
            j = Hexadecimal.convert_from_denary_to_octadecimal(j)
            print("The hexadecimal equivalent of ", self.biny,"in octadecimal is",j)
