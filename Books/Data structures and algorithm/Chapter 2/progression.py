
class Progression:
    """ Iterator producing a generic progression.

    Default iterator produces the whole number 0, 1, 2, ...
    """

    def __init__(self, start=0):
        """Initialize current to the firsy value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.

        This should be overridden by a subclass to customize progression

        By convention, if current is set to None, this designates the
        end of a finite progression
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current 
            sel
