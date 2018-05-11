import sympy


def equation_to_expression(equation):
    try:
        expression = sympy.simplify(equation)
    except ValueError:
        raise ValueError("Not a valid function")
    return expression


def get_symbol(expression):
    if len(expression.free_symbols) != 1:
        raise ValueError("Not a valid function")
    return expression.free_symbols.pop()


def expression_to_lambda(x, expression):
    try:
        func = sympy.lambdify(x, expression)
    except ValueError:
        raise ValueError("Not a valid function")
    return func

def to_polynomial(expression, num_terms=10):
    try:
        x = get_symbol(expression)
        poly_terms = []
        fact = 1;
        for i in range(num_terms):
            func = expression_to_lambda(x, expression)
            poly_terms.append(func(0) / fact)
            fact *= (i + 1)
            expression = sympy.diff(expression, x)
        return poly_terms
    except ValueError:
        raise ValueError("Not a valid function")