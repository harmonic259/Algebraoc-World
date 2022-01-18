class Polynomial:
    def __init__(self, coefficients, degree):
        self.coefficients = coefficients
        self.degree = degree

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




