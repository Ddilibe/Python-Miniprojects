from Formular.error import BaseError
from Formular.baser import BaseConvert



class Binary(BaseError, BaseConvert):

    def __init__(self, biny, num):
        self.biny = biny
        self._num = num

    def start(self,):
        try:
            self.biny = Binary.convert_int_to_list(str(self.biny))
            check = Binary.error_binary(self.biny)
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
        except(ValueError):
            return "NONUM" #That's not a number at all

    def confirm(self, ):
        j = Binary.convert_from_binary_to_denary(self.biny)
        if self._num == 0:
            pass
        if self._num == 1:
            j = Binary.convert_from_denary_to_octadecimal(j)
        if self._num == 2:
            j = Binary.convert_from_denary_to_hexadecimal(j)
        return j
    
