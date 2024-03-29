from matplotlib import pyplot as plt

class AlphabetFrequency:
    """ Reads the content of a file 
        
        _________________________
        Requirement: Matplotlib

        ________________________________
        Install: pip3 install matplotlib

        Displays a barchart of the frequency of each alphabet from a document
    """

    value, alpha = [], ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def __init__(self, file):
        """Recieves the file
        Parameter:
        file    Contains the file needing analysis
        _______
        Caution
        Make sure that the file is in the same directory else it won't work
        """
        self._file = file
        with open(self._file, 'r') as op:
            ch = op.read()
            self.parse_data(ch)
            op.close()

    def fullup(self):
        """ Method for filling empty databases """
        for i in range(len(AlphabetFrequency.alpha)):
                AlphabetFrequency.value.append(int(0))

    def parse_data(self,op):
        """ Method Used to parse through data and update the list"""
        self.fullup()
        for i in op:
            h = 0
            for e in range(26):
                if i.upper() == AlphabetFrequency.alpha[e]:
                    AlphabetFrequency.value[e] += 1
                    h += 1
                    break

    def display_chart(self):
        """ Method used to display the chart after analysis"""
        xs, top = [], []
        for i in range(26):
            try:
                if  AlphabetFrequency.value[i] > 0:
                    xs.append(AlphabetFrequency.alpha[i])
                    top.append(AlphabetFrequency.value[i])
            except IndexError:
                break
        plt.xlabel(f"ALphabets contained in {self._file}")
        plt.ylabel("Number of times the alphabet occured")
        plt.title(f"A graph of a alphabet appearance frequency of the file {self._file}")
        plt.bar(xs, top)
        plt.savefig(f"{self._file}.png")
        plt.show()

if __name__ == '__main__':
    jo = AlphabetFrequency("python.xml")
    jo.display_chart()

    jo = AlphabetFrequency("range.py")
    jo.display_chart()

    jo = AlphabetFrequency("Polynomial.py")
    jo.display_chart()

    jo = AlphabetFrequency("sequence.py")
    jo.display_chart()

    jo = AlphabetFrequency("credit_card.py")
    jo.display_chart()
