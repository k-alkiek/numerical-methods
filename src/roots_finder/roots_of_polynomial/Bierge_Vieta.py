import numpy
import timeit
from src.roots_finder.equations_parser import *


class BiergeVieta:
    def solve(self, equation, *args, max_iterations=50, epsilon=0.0001):
        if len(args) < 1:
            raise TypeError("Missing arguments")
        current_approx = args[0]
        if len(args) > 1:
            max_iterations = args[1]
        if len(args) > 2:
            epsilon = args[1]
        number_of_iterations = 0
        start_time = timeit.default_timer()
        # Parsing string into a func using Sympy lib and throw exception if the function not valid
        try:
            expression = equation_to_expression(equation)
            polynomial = sympy.Poly(expression)
            poly_coefficients = numpy.array(polynomial.all_coeffs())
        except ValueError:
            raise ValueError("Not a valid function")

        len_of_poly = len(poly_coefficients)
        approximate_root = 0
        error = 100
        iterations = []
        # Iterations
        while error >= epsilon and number_of_iterations <= max_iterations:
            horner_coeffs = numpy.zeros(len_of_poly, dtype=float)  # b's array
            derivative_coeffs = numpy.zeros(len_of_poly - 1, dtype=float)  # c's array
            # Calculate b array
            horner_coeffs[0] = poly_coefficients[0]
            for i in range(1, len_of_poly):
                b = float(poly_coefficients[i] + current_approx * horner_coeffs[i - 1])
                horner_coeffs[i] = b
            # Calculate c array
            derivative_coeffs[0] = horner_coeffs[0]
            for i in range(1, len_of_poly - 1):
                c = horner_coeffs[i] + current_approx * derivative_coeffs[i - 1]
                derivative_coeffs[i] = c
            # Calculate next approximation of root
            displacement = horner_coeffs[-1] / derivative_coeffs[-1]
            approximate_root = current_approx - displacement
            error = abs((approximate_root - current_approx) / approximate_root) * 100
            # TODO adding iterations
            iteration = numpy.array((poly_coefficients, horner_coeffs, derivative_coeffs, approximate_root, error),
                                    dtype=[('a', numpy.array()), ('b', numpy.array()), ('c', numpy.array()),
                                           ('approx_root', numpy.float), ('err', numpy.float)])
            iterations.append(iteration)
            current_approx = approximate_root
            number_of_iterations += 1

        execution_time = timeit.default_timer() - start_time
        if number_of_iterations > max_iterations:
            raise ValueError("Bierge Vieta method can't find a root for this function")

        return number_of_iterations, execution_time, iterations, approximate_root, error
