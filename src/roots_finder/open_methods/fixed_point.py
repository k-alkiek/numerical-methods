import numpy
import timeit
from src.roots_finder.equations_parser import *


class FixedPoint:
    def solve(self, equation, *args, max_iterations=50, epsilon=0.0001):
        if len(args) < 1:
            raise TypeError("Missing arguments")
        approximate_root = args[0]
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
            expression = sympy.Add(x, -expression)
            func = expression_to_lambda(x, -expression)
        except ValueError:
            raise ValueError("Not a valid function")
        prev_approx = approximate_root
        error = 100
        iterations = []
        # Iterations
        while True:
            approximate_root = func(prev_approx)
            error = abs((approximate_root - prev_approx) / approximate_root) * 100

            iteration = numpy.array((prev_approx, approximate_root, error),
                                    dtype=[('prev_approx', numpy.float), ('approx_root', numpy.float),
                                           ('err', numpy.float)])
            iterations.append(iteration)
            prev_approx = approximate_root
            number_of_iterations += 1
            # if error >= 100:
            #     raise ValueError("Fixed point method can't find a root for this initial value, may be diverged")

            if error < epsilon or number_of_iterations > max_iterations:
                break

        execution_time = timeit.default_timer() - start_time
        print(func(1))
        return number_of_iterations, execution_time, iterations, approximate_root, error, func
