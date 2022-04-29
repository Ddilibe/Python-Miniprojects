from Formular.error import BaseError
from Formular.baser import BaseConvert

class Denary(BaseError, BaseConvert):

    def __init__(self, biny, num ):
        self.biny = biny
        self._num = num

    def start(self,):
        try: 
            self.biny = Denary.convert_int_to_list(self.biny)
            check = Denary.error_denary(self.biny)
            if check == False:
                return "NOBIN" #Those are not binary numbers
            else:
                try:
                    if (0<=self._num<3):
                        return (self.confirm(self.biny))
                    else:
                        return "NORAN" #Option not in the range
                except (ValueError, TypeError):
                    return "NONUM" #This is not a number at all
        except (ValueError, TypeError):
            return "NONUM" #That's not a number at all

    def confirm(self,ju ):
        if self._num == 0:
            j = Denary.convert_from_denary_to_binary(ju)
        if self._num == 1:
            j = Denary.convert_from_denary_to_octadecimal(ju)
        if self._num == 2:
            j = Denary.convert_from_denary_to_hexadecimal(ju)
        return j
