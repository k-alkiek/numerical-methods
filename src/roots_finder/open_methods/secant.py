import sympy
import numpy
import timeit


class Secant:
    def solve(self, equation, cur_value, prev_value, max_iterations=50, epsilon=0.0001):
        number_of_iterations = 0
        start_time = timeit.default_timer()
        # Parsing string into a func using Sympy lib and throw exception if the function not valid
        try:
            expression = sympy.simplify(equation)
            x = expression.free_symbols.pop()
            func = sympy.lambdify(x, expression)
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
            # iterations.append(iteration)
            prev_value = cur_value
            cur_value = approximate_root
            number_of_iterations += 1
        execution_time = timeit.default_timer() - start_time
        if number_of_iterations > max_iterations:
            raise ValueError("Secant method can't find a root for this function")

        return number_of_iterations, execution_time, iterations, approximate_root, error
