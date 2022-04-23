
class Vector:
    """ Represent a vector in a multidimentional space """

    def __init__(self, d):
        """ Create d-dimentional vector of zeros. """
        self._coords = [0] * d

    def __len__(self):
        """ Return the dimention of the vector. """
        return len(self._coords)

    def __getitem__(self, j):
        """ Return jth coordinate of a vector """
        return self._coords[j]

    def __setitem__(self, j, val):
        """ Set jth coordinate of vector to given value. """
        self._coords[j] = val

    def __add__(self, other):
        """ Return sum of two vectors """
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """ Return True if vectors has the same cooridinate as others. """
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vectors differ from other. """
        return not self == other            # rely on exsiting __eq__ definition

    def __str__(self):
        """ Produce string representation of vector. """
        return '<' + str(self._coords)[1:-1] + '>'

f = Vector(2)
print(f)
