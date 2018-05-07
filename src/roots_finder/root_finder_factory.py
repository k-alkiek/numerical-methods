from src.roots_finder.bracketing_methods.bisection import Bisection
from src.roots_finder.bracketing_methods.regula_falsi import FalsePosition
from src.roots_finder.open_methods.fixed_point import FixedPoint
from src.roots_finder.open_methods.secant import Secant
from src.roots_finder.open_methods.Newton_Raphson import NewtonRaphson
from src.roots_finder.open_methods.first_modified_Newton import FirstModifiedNewton
from src.roots_finder.open_methods.second_modified_Newton import SecondModifiedNewton
from src.roots_finder.roots_of_polynomial.Bierge_Vieta import BiergeVieta


class RootFinderFactory:
    def solve(self, method_name, equation, *args):
        solver = None
        if method_name == "Bisection":
            solver = Bisection();
        elif method_name == "False position":
            solver = FalsePosition()
        elif method_name == "Fixed point":
            solver = FixedPoint()
        elif method_name == "Secant":
            solver = Secant()
        elif method_name == "Newton Raphson":
            solver = NewtonRaphson()
        elif method_name == "First modified Newton":
            solver = FirstModifiedNewton()
        elif method_name == "Second modified Newton":
            solver = SecondModifiedNewton()
        elif method_name == "Bierge Vieta":
            solver = BiergeVieta()
        return solver.solve(equation, args)
