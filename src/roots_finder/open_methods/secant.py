import numpy
import timeit
from src.roots_finder.equations_parser import *


class Secant:
    def solve(self, equation, *args, max_iterations=50, epsilon=0.0001):
        if len(args) < 2:
            raise TypeError("Missing arguments")
        cur_value = args[0]
        prev_value = args[1]
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
            func = expression_to_lambda(x, expression)
        except ValueError:
            raise ValueError("Not a valid function")
        approximate_root = 0
        error = 100
        iterations = []
        # Iterations
        while error >= epsilon and number_of_iterations <= max_iterations:
            displacement = (func(cur_value) * (prev_value - cur_value)) / (func(prev_value) - func(cur_value))
            approximate_root = cur_value - displacement
            error = abs((approximate_root - cur_value) / approximate_root) * 100
            # TODO adding iterations
            iteration = numpy.array((prev_value, cur_value, approximate_root, error),
                                    dtype=[('prev', numpy.float), ('cur', numpy.float), ('approx', numpy.float),
                                           ('err', numpy.float)])
            iterations.append(iteration)
            prev_value = cur_value
            cur_value = approximate_root
            number_of_iterations += 1
        execution_time = timeit.default_timer() - start_time
        if number_of_iterations > max_iterations:
            raise ValueError("Secant method can't find a root for this function")

        return number_of_iterations, execution_time, iterations, approximate_root, error, func
