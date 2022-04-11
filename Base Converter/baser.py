from error import BaseError


class BaseConvert():
    """
        BaseConvert converts all the bases in denary to the different bases
        BaseConvert also converts all other different bases into denary
    """

    @classmethod
    def convert_int_to_list(cls, j):
        """
            converts all input into a list
        """
        w = []
        d = ''
        while j != 0:
            w.append(str(j % 10))
            j = int( j /10)
        w.reverse()
        w = ''.join(w)
        return w

    @classmethod 
    def convert_from_binary_to_denary(cls, j):
        """
            Converts binary to denary
        """     
        w = 0
        j = list(j)
        f = len(j) - 1
        for i in j:
            w += int(i) * (2 ** f)
            f -= 1
        return w

    @classmethod
    def convert_from_hexadecimal_to_denary(cls, j):
        """
            Converts Hexadecimal to denary
        """
        w = 0
        j = list(j)
        f = len(j) - 1
        for i in j:
            i = i.upper()
            if i == 'A':
                w += 10 * (16 ** f)
            elif i == 'B':
                w += 11 * (16 ** f)
            elif i == 'C':
                w += 12 * (16 ** f)
            elif i == 'D':
                w += 13 * (16 ** f)
            elif i == 'E':
                w += 14 * (16 ** f)
            elif i == 'F':
                w += 15 * (16 ** f)
            else:
                w += int(i) * (16 ** f)
            f -= 1
        return w

    @classmethod
    def convert_from_octadecimal_to_denary(cls, j):
        """     
            Converts octadecimal to denary
        """
        w = 0
        j = list(j)
        f = len(j) - 1
        for i in j:
            w += int(i) * (8 ** f)
            f -= 1
        return w

    @classmethod
    def convert_from_denary_to_binary(cls, j):
        """
            Converts from denary to binary
        """
        w = []
        while j != 0:
            w.append(j % 2) 
            j = int(j / 2)
        w.reverse()
        d = ''
        for i in w:
            d += str(i)
        w = int(d)
        return w

    @classmethod
    def convert_from_denary_to_octadecimal(cls, j):
        """
            Converts from denary to octadecimal
        """
        w = []
        while j != 0:
            w.append(j % 8)
            j = int(j / 8)
        w.reverse()
        d = ''
        for i in w:
            d += str(i)
        w = int(d)
        return w

    @classmethod
    def convert_from_denary_to_hexadecimal(cls, j):
        """
            Converts from denary to hexadecimal
        """
        w = []
        while j != 0:
            e = (j % 16)
            j = int(j / 16)
            if e == 10:
                w.append('A')
            elif e == 11:
                w.append('B')
            elif e == 12:
                w.append('C')
            elif e == 13:
                w.append('D')
            elif e == 14:
                w.append('E')
            elif e == 15:
                w.append('F')
            else:
                w.append(str(e))
        w.reverse()
        w = "".join(w)
        return w
