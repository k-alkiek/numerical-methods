import sympy


def add_symbols_to_set(symbolSet, symbols):
    for symbol in symbols:
        symbolSet.add(symbol)


def equations_to_matrix(equations):
    symbols = set()
    system = []
    for equation in equations:
        sides = equation.split("=")
        LHS, RHS = sides
        expression = sympy.Eq(sympy.simplify(LHS), sympy.simplify(RHS))
        system.append(expression)
        add_symbols_to_set(symbols, expression.free_symbols)
    symbols = sorted(list(symbols), key=str)
    coeffs, b = sympy.linear_eq_to_matrix(system, symbols)
    return coeffs, b, symbols, system


class GaussJordan:
    def solve(self, equations):
        try:
            system = equations_to_matrix(equations)
        except ValueError:
            raise ValueError("Not a valid system")
        coefficients = system[0]
        rhs = system[1]
        symbols = system[2]
        eqs = system[3]
        n = len(equations)
        for k in range(n):
            for i in range(n):
                if i == k:
                    continue
                factor = coefficients[i, k] / coefficients[k, k]
                for j in range(n):
                    coefficients[i, j] -= factor * coefficients[k, j]
                rhs[i, 0] -= factor * rhs[k, 0]
        ans = []
        for i in range(n):
            ans.append((symbols[i], float(rhs[i, 0] / coefficients[i, i])))
        return ans, eqs


solver = GaussJordan()
equations = ["x + y + 2 * z = 8", "-1 * x -2 * y + 3 * z = 1", "3 * x + 7 * y + 4 * z = 10"]
print(solver.solve(equations))
