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
