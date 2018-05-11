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
        if n != len(symbols) or coefficients.det() == 0:
            raise ValueError("The system has not a unique solution")

        for k in range(n):
            max_elem_index = self.__pivoting(coefficients, k)
            coefficients.row_swap(max_elem_index, k)
            rhs.row_swap(max_elem_index, k)
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

    def __pivoting(self, matrix: sympy.Matrix, row_index):
        max_index = row_index
        pivot = abs(matrix[row_index, row_index])
        rows = matrix.shape[0]
        for i in range(row_index, rows):
            if abs(matrix[i, row_index]) > pivot:
                max_index = i
                pivot = abs(matrix[i, row_index])
        return max_index
