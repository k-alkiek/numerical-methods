import numpy
import timeit
from src.roots_finder.equations_parser import *


class FirstModifiedNewton:
    # First modified Newton Raphson method to get multiple root
    def solve(self, equation, *args, max_iterations=50, epsilon=0.0001):
        if len(args) < 2:
            raise TypeError("Missing arguments")
        current_approx = args[0]
        m = args[1]
        if len(args) > 2:
            max_iterations = args[2]
        if len(args) > 3:
            epsilon = args[3]
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
            approximate_root = current_approx - m * displacement
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
