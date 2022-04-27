from Formular.baser import BaseConvert
from Formular.error import BaseError

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

mon = Hexadecimal()
mon.confirm()

