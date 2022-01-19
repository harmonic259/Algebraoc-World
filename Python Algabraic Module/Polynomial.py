class Polynomial:
    def __init__(self, coefficients, degree):
        self.coefficients = coefficients
        self.degree = degree

    def set(self, poly):
        self.coefficients = poly.coefficients
        self.degree = poly.degree

    def get_coefficients(self):
        return self.coefficients

    def print_polynomial(self):
        i = 0
        for c in self.coefficients:
            if c == self.coefficients[self.degree]:
                print(str(c)+"*x^"+str(i), end=" ")
            elif c == self.coefficients[0]:
                print(str(c) + " +", end=" ")
            else:
                print(str(c) + "*x^" + str(i) + " +", end=" ")
            i = i + 1

    def value(self, x):
        ans = 0
        i = 0
        for c in self.coefficients:
            ans = ans + c*(x ** i)
            i = i + 1
        return ans

    def derivative(self):
        new_coeff = []
        new_deg = self.degree - 1
        c = 1
        for x in self.coefficients:
            if x != self.coefficients[0]:
                new_coeff = new_coeff + [c*x]
                c = c + 1
        ans_poly = Polynomial(new_coeff, new_deg)
        return ans_poly

    def integral(self):
        new_coeff = [0]
        new_deg = self.degree - 1
        c = 1
        for x in self.coefficients:
            new_coeff = new_coeff + [x / c]
            c = c + 1
        ans_poly = Polynomial(new_coeff, new_deg)
        return ans_poly








