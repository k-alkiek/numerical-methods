import sympy
import mpmath
from src.roots_finder.equations_parser import *

class General_Algorithm:


    def solve(self, equation, num_terms=10, num_iterations=100):
        expression = equation_to_expression(equation)
        coefficients = to_polynomial(expression, num_terms)
        poly_sols = solve_polynomial(coefficients, num_iterations)
        for i in range(len(poly_sols)):
            print(poly_sols[i]);
            #solve by newton


def solve_polynomial(coefficients, num_iterations=1000, roots_prev=[]):
    n = len(coefficients)
    while (True):
        if (abs(coefficients[n - 1]) < 10 ** -5):
            coefficients = coefficients[:n - 1]
            n = len(coefficients)
        else:
            break
    for i in range(n):
        coefficients[i] /= coefficients[n - 1]

    def f_(x):
        res = 0
        tmp = 1
        for i in range(n):
            res += coefficients[i] * tmp
            tmp *= x
        return res

    if (len(roots_prev) == 0):
        first_root = randint(2, 10)
        roots_prev = [first_root]  # intial guess
        for i in range(1, n - 1):
            roots_prev.append(roots_prev[i - 1] * first_root)
    roots_next = [None] * (n - 1)
    for it in range(num_iterations):
        for i in range(n - 1):
            denominator = 1
            for j in range(n - 1):
                if (i != j):
                    denominator *= (roots_prev[i] - roots_prev[j])
            roots_next[i] = roots_prev[i] - f_(roots_prev[i]) / denominator
        roots_prev = list(roots_next)
    return roots_next