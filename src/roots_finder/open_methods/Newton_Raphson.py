import sympy
import numpy
import timeit


class NewtonRaphson:
    # TODO adding modified Newton Raphson algorithms
    def solve(self, equation, current_approx, max_iterations=50, epsilon=0.0001):
        number_of_iterations = 0
        start_time = timeit.default_timer()
        # Parsing string into a func using Sympy lib and throw exception if the function not valid
        try:
            expression = sympy.simplify(equation)
            x = expression.free_symbols.pop()
            derivative = sympy.diff(expression, x)
            func = sympy.lambdify(x, expression)
            diff = sympy.lambdify(x, derivative)
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
            # iterations.append(iteration)
            current_approx = approximate_root
            number_of_iterations += 1
        execution_time = timeit.default_timer() - start_time
        if number_of_iterations > max_iterations:
            raise ValueError("Secant method can't find a root for this function")

        return number_of_iterations, execution_time, iterations, approximate_root, error
