import random
from src.roots_finder.open_methods.Newton_Raphson import *
from src.general_algorithm.delete_dublication import *
import timeit

class general_algorithm:

    def solve(self, equation, num_iterations=100,epsilon=10**-5, num_terms=10):
        start_time = timeit.default_timer()
        expression = equation_to_expression(equation)
        x = get_symbol(expression)
        func = expression_to_lambda(x, expression)
        coefficients = to_polynomial(expression, num_terms)
        makluin_func = lambda x: polynomial_calculater(coefficients, x)
        poly_sols = solve_polynomial(coefficients, num_iterations=num_iterations)
        solver = NewtonRaphson()
        float_set = delete_dublication()
        float_set.set_epsilon(epsilon)
        for i in range(len(poly_sols)):
            cur_solution = solver.solve(equation, poly_sols[i])[3]
            if(abs(func(cur_solution)) < epsilon):      #if this solution is zero
                float_set.add_element(cur_solution)
        roots = float_set.get_elements()
        execution_time = timeit.default_timer() - start_time
        return num_iterations, roots, execution_time, func, makluin_func


def polynomial_calculater(coefficients, x):
    n = len(coefficients)
    res = 0
    tmp = 1
    for i in range(n):
        res += coefficients[i] * tmp
        tmp *= x
    return res

# Remvoe Zeros in the last coefficients and set the last coefficients equal to 1
def reduce_polynomial(coefficients):
    n = len(coefficients)
    while (True):
        if (abs(coefficients[n - 1]) < 10 ** -5):
            coefficients = coefficients[:n - 1]
            n = len(coefficients)
        else:
            break
    for i in range(n):
        coefficients[i] /= coefficients[n - 1]
    return coefficients

def solve_polynomial(coefficients, num_iterations=100, roots_prev=[]):
    coefficients = reduce_polynomial(coefficients)
    n = len(coefficients)
    # Initialization The First Guess
    if (len(roots_prev) == 0):
        roots_prev = []
        for i in range(1, n):
            roots_prev.append(i)
    # Iterate
    roots_next = [None] * (n - 1)
    for it in range(num_iterations):
        for i in range(n - 1):
            denominator = 1
            for j in range(n - 1):
                if (i != j):
                    denominator *= (roots_prev[i] - roots_prev[j])
            roots_next[i] = roots_prev[i] - polynomial_calculater(coefficients, roots_prev[i]) / denominator
        roots_prev = list(roots_next)

    return roots_next