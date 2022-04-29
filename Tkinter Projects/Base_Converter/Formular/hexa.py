from Formular.baser import BaseConvert
from Formular.error import BaseError

class Hexadecimal(BaseConvert, BaseError):

    def __init__(self, biny, num):
        self.biny = biny
        self._num = num


    def start(self,):
        try:
            check = Hexadecimal.error_hexa(self.biny)
            if check == False:
                return "NOBIN" #Those are not binary numbers
            else:
                try:
                    if (0<=self._num<3):
                        return (self.confirm())
                    else:
                        return "NORAN" #Option not in the range
                except (ValueError, TypeError):
                    return "NONUM" #This is not a number at all
        except (ValueError, TypeError):
            return "NONUM" #That's not a number at all

    def confirm(self,):
        j = Hexadecimal.convert_from_hexadecimal_to_denary(self.biny)
        if self._num == 0:
            pass
        if self._num == 1:
            j = Hexadecimal.convert_from_denary_to_binary(j)
        if self._num == 2:
            j = Hexadecimal.convert_from_denary_to_octadecimal(j)
        return j
