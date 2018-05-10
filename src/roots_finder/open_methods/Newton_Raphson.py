import numpy
import timeit
from src.roots_finder.equations_parser import *


class NewtonRaphson:
    # TODO adding modified Newton Raphson algorithms
    def solve(self, equation, *args, max_iterations=50, epsilon=0.0001):
        if len(args) < 1:
            raise TypeError("Missing arguments")
        current_approx = args[0]
        if len(args) > 1:
            max_iterations = args[1]
        if len(args) > 2:
            epsilon = args[2]

        number_of_iterations = 0
        start_time = timeit.default_timer()
        # Parsing string into a func using Sympy lib and throw exception if the function not valid
        try:
            expression = equation_to_expression(equation)
            x = get_symbol(expression)
            derivative = sympy.diff(expression, x)
            func = expression_to_lambda(x, expression)
            diff = expression_to_lambda(x, derivative)
        except ValueError:
            raise ValueError("Not a valid function")
        approximate_root = 0
        error = 100
        iterations = []
        while error >= epsilon and number_of_iterations <= max_iterations:
            displacement = func(current_approx) / diff(current_approx)
            approximate_root = current_approx - displacement
            error = abs((approximate_root - current_approx) / approximate_root) * 100
            # TODO adding iterations
            iteration = numpy.array((current_approx, approximate_root, error),
                                    dtype=[('cur_approx', numpy.float), ('approx_root', numpy.float),
                                           ('err', numpy.float)])
            iterations.append(iteration)
            current_approx = approximate_root
            number_of_iterations += 1
        execution_time = timeit.default_timer() - start_time
        if number_of_iterations > max_iterations:
            raise ValueError("Secant method can't find a root for this function")

        return number_of_iterations, execution_time, iterations, approximate_root, error, func
