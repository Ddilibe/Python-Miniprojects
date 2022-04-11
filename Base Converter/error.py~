

class BaseError():
    """
        Error handling instance for the base converter
    """
    binny = [0,1]
    octa = [0,1,2,3,4,5,6,7]
    den = [0,1,2,3,4,5,6,7,8,9]
    hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

    @classmethod
    def error_binary(cls, j):
        j = list(j)
        while True:
            for i in j:
                if int(i) in BaseError.binny:
                    pop = True
                    continue
                else:
                    pop = False
                    break
            break
        return pop

    @classmethod
    def error_denary(cls, g):
        g = list(g)
        while True:
            for i in g:
                if int(i) in BaseError.den:
                    pop = True
                    continue
                else: 
                    pop = False
                    break
            break
        return pop

    @classmethod
    def error_hexa(cls, g):
        g = list(g)
        while True:
            for i in g:
                if str(i).upper() in BaseError.hexa:
                    pop = True
                    continue
                else:
                    pop = False
                    break
            break
        return pop

    @classmethod
    def error_octa(cls, g):
        g = list(g)
        while True:
            for i in g:
                if int(i) in BaseError.octa:
                    pop = True
                    continue
                else:
                    pop = False
                    break
            break
        return pop
