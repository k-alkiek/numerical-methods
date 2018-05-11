import re
from enum import IntEnum
from textwrap import dedent

from sympy import Eq
from sympy.parsing.sympy_parser import parse_expr


class RootFindingMethod(IntEnum):
    BISECTION = 1
    FALSE_POSITION = 2
    FIXED_POINT = 3
    NEWTON_RAPHSON = 4
    SECANT = 5
    BIERGE_VIETA = 6
    GENERAL_ALGORITHM = 7


class InterpolationMethod(IntEnum):
    NEWTON = 1
    LAGRANGE = 2


list_of_points_regex = re.compile(r'^\[(.*)\]$')


def remove_spaces(string):
    return re.sub(r'\s+', '', string)


def get_list_of_points(string, count=0):
    match = list_of_points_regex.match(remove_spaces(string))
    if not match:
        raise ValueError('Malformed parameters: ' + string)
    points = list(map(float, match[1].split(',')))
    if count and not len(points) == count:
        raise ValueError('Expected ' + str(count) +
                         ' points, got ' + str(len(points)))
    return points


def get_interval(string):
    try:
        interval = get_list_of_points(string, 2)
    except ValueError:
        raise ValueError('Expected an interval, got: ' + string)
    return interval


def parse_root_finder_file(path):
    file = open(path)

    expected = dedent('''\
            Expected an integer between 1 and 7 as follows:
            1) Bisection method
            2) False-position method
            3) Fixed-point method
            4) Newton-Raphson method
            5) Secand method
            6) Bierge-Vieta method
            7) General algorithm''')
    try:
        method = int(file.readline().strip())
    except ValueError:
        raise ValueError(expected)
    if method not in list(map(int, RootFindingMethod)):
        raise ValueError(expected)

    try:
        equation = Eq(parse_expr(file.readline()))
    except SyntaxError as ex:
        raise ValueError('Malformed equation: ' + ex.msg)
    if not len(equation.free_symbols) == 1:
        raise ValueError('Equation should contain exactly one symbol')

    last_pos = file.tell()
    parameters = file.readline().strip()
    try:
        if method == RootFindingMethod.BISECTION:
            parameters = get_interval(parameters)
        elif method == RootFindingMethod.FALSE_POSITION:
            parameters = get_interval(parameters)
        elif method == RootFindingMethod.FIXED_POINT:
            parameters = [float(parameters)]
        elif method == RootFindingMethod.NEWTON_RAPHSON:
            parameters = [float(parameters)]
        elif method == RootFindingMethod.SECANT:
            parameters = list(map(float, parameters.split()))
        elif method == RootFindingMethod.BIERGE_VIETA:
            parameters = [float(parameters)]
        elif method == RootFindingMethod.GENERAL_ALGORITHM:
            file.seek(last_pos)
    except ValueError:
        raise ValueError('Malformed parameters, expected decimals')

    expected = 'Expected a positive decimal representing tolerance'
    try:
        tolerance = float(file.readline().strip())
    except ValueError:
        raise ValueError(expected)
    if tolerance <= 0:
        raise ValueError(expected)

    expected = 'Expected a positive integer representing the maximum'
    'number of iterations'
    try:
        iterations = int(file.readline().strip())
    except ValueError:
        raise ValueError(expected)
    if iterations <= 0:
        raise ValueError(expected)

    file.close()
    return {
        'method': method,
        'equation': equation,
        'parameters': parameters,
        'tolerance': tolerance,
        'iterations': iterations
    }


def parse_interpolation_file(path):
    file = open(path)

    expected = dedent('''\
            Expected an integer between 1 and 2 as follows:
            1) Newton's divided difference method
            2) Lagrange method''')
    try:
        method = int(file.readline().strip())
    except ValueError:
        raise ValueError(expected)
    if method not in list(map(int, InterpolationMethod)):
        raise ValueError(expected)

    expected = 'Expected a positive integer representing'
    'the number of points used in interpolation'
    try:
        order = int(file.readline().strip())
    except ValueError:
        raise ValueError(expected)
    if order <= 0:
        raise ValueError(expected)

    x_coords = get_list_of_points(file.readline().strip(), order)
    y_coords = get_list_of_points(file.readline().strip(), order)
    query_points = get_list_of_points(file.readline().strip())

    file.close()
    return {
        'method': method,
        'order': order,
        'points': list(zip(x_coords, y_coords)),
        'query_points': query_points
    }


def parse_equations_file(path):
    file = open(path)
    try:
        equations = [Eq(line) for line in file]
    except SyntaxError as ex:
        raise ValueError('Malformed equation: ' + ex.msg)
    file.close()
    return equations
