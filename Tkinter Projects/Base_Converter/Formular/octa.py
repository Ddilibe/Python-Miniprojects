from Formular.error import BaseError
from Formular.baser import BaseConvert



class Octadecimal(BaseError, BaseConvert):
    
    def __init__(self, biny, num):
        self.biny = biny
        self._num = num

    def start(self,):
        try: 
            self.biny = Octadecimal.convert_int_to_list(self.biny)
            check = Octadecimal.error_octa(self.biny)
            if check == False:
                return "NOBIN" #Those are not binary numbers
            else:
                try:
                    if (0<=self._num<3):
                        return (self.Confirm())
                    else:
                        return "NORAN" #Option not in the range
                except (ValueError, TypeError):
                    return "NONUM" #This is not a number at all
        except (ValueError, TypeError):
            return "NONUM" #That's not a number at all
        
    def Confirm(self,):
        j = Octadecimal.convert_from_octadecimal_to_denary(self.biny)
        if self._num == 0:
            pass
        if self._num == 1:
            j = Octadecimal.convert_from_denary_to_binary(j)
        if self._num == 2:
            j = Octadecimal.convert_from_denary_to_hexadecimal(j)
        return j
