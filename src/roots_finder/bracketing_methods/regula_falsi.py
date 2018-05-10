import numpy
import timeit
from src.roots_finder.equations_parser import *


class FalsePosition:
    def solve(self, equation, *args, max_iterations=50, epsilon=0.0001):
        if len(args) < 2:
            raise TypeError("Missing arguments")
        left = args[0]
        right = args[1]
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
        prev_approx = 0
        error = 0
        iterations = []  # Iteration array to store each iteration
        # Iterations
        while abs(right - left) >= epsilon and number_of_iterations <= max_iterations:
            left_value, right_value = func(left), func(right)
            # Handling if this interval has odd roots between left and and right (At least one root)
            if left_value * right_value > 0:
                raise ValueError("False position method can't find a root for this interval")
            # Calculate approximate value of root
            approximate_root = (left * right_value - right * left_value) / (right_value - left_value)
            approximate_root_value = func(approximate_root)
            # Determine the next interval
            if approximate_root_value * left_value < 0:
                right = approximate_root
            elif approximate_root_value * left_value > 0:
                left = approximate_root
            else:
                break
            error = abs((approximate_root - prev_approx) / approximate_root) * 100
            # TODO adding iterations
            iteration = numpy.array((left, right, approximate_root, error),
                                    dtype=[('xl', numpy.float), ('xu', numpy.float), ('xr', numpy.float),
                                           ('err', numpy.float)])
            iterations.append(iteration)
            prev_approx = approximate_root
            number_of_iterations += 1

        execution_time = timeit.default_timer() - start_time

        if number_of_iterations > max_iterations:
            raise ValueError("False position method can't find a root for this function")

        return number_of_iterations, execution_time, iterations, approximate_root, error, func
