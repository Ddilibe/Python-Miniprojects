

class Polynomial:
    """ Finding the First derivative of a polynomial equation

    The equation will be in the form "2x2 + 3X + 4"
    """
    equation_in_list = []
    alpha_list = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    solved_equation = []

    def __init__(self, equation, point = 1):
        """
        This section can not be overridden

        equation    Contains the polynomial equation
        """
        self.equation = equation
        self.point = point

    def __len__(self):
        """Returns the number of unknowns in a polynomial set """
        return (len(equation_in_list) - 1)

    def creating_equation_list(self):
        """ Does not return anything. Creates the polynomial equation """
        equation_parts = list(self.equation)
        equat = []
        for i in equation_parts:
            if i == ('+' or '-'):
                Polynomial.equation_in_list.append(equat)
                equat = []
                equat.append(i)
            else:
                equat.append(i)
        Polynomial.equation_in_list.append(equat)

    def creates_the_derivative(self):
        """ Returns the dervative of the equation Passed"""
        self.creating_equation_list()
        y, a, u, q, w = 0, '', -1, 0, ''
        for i in Polynomial.equation_in_list:
            final = []
            for j in i:
                if j in ('+','-'):
                    w = j
                else:
                    try:
                        int(j)
                        y = (y * 10) + int(j)
                    except ValueError:
                        if j.upper() in Polynomial.alpha_list:
                            a += a
                    break
            while True:
                try:
                    int(q)
                    q = (q * 10) + int(i[u])
                    u -= 1
                except ValueError:
                    break
            if not(a == ''):
                y *= q
                q -= 1
            if not((a == '') or (q < 1)):
                final.append(str(y) + a + str(q))
            elif q == 1:
                final.append(str(y) + a)
            elif q <= 0:
                final.append(str(y))
            elif a == '':
                continue
            else:
                continue
            Polynomial.solved_equation.append(w)
            Polynomial.solved_equation.append(final)
        return (Polynomial.solved_equation)

    def get_solution(self):
        t = ""
        self.creates_the_derivative()
        for i in Polynomial.solved_equation:
            for j in i:
                t += str(" ") + str(j)
        return t

    def print_solution(self):
        t = self.get_solution()
        print(f"The {self.point} derivative of {self.equation} is {t}")

if __name__ == '__main__':
    print("Just Testing the equation a unique way")
    J = Polynomial('2x + 1')
    J.print_solution()
