import sympy
import timeit


class FixedPoint:
    def solve(self, equation, approximate_root, max_iterations=50, epsilon=0.0001):
        number_of_iterations = 0
        start_time = timeit.default_timer()
        # Parsing string into a func using Sympy lib and throw exception if the function not valid
        try:
            expression = sympy.simplify(equation)
            x = expression.free_symbols.pop()
            expression = sympy.Add(x, -expression)
            func = sympy.lambdify(x, expression)
        except ValueError:
            raise ValueError("Not a valid function")
        prev_approx = approximate_root
        error = 100
        iterations = []
        # Iterations
        while error >= epsilon and number_of_iterations <= max_iterations:
            approximate_root = func(prev_approx)
            error = abs((approximate_root - prev_approx) / approximate_root) * 100
            # TODO adding iterations
            # iterations.append(iteration)
            prev_approx = approximate_root
            number_of_iterations += 1
            if error >= 100:
                raise ValueError("Fixed point method can't find a root for this initial value, may be diverged")

        execution_time = timeit.default_timer() - start_time

        if number_of_iterations > max_iterations:
            raise ValueError("Fixed point method can't find a root for this function")

        return number_of_iterations, execution_time, iterations, approximate_root, error
