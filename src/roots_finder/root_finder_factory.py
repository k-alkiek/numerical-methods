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
        if method_name == "Bisection" or method_name == "1":
            solver = Bisection()
        elif method_name == "False position" or method_name == "2":
            solver = FalsePosition()
        elif method_name == "Fixed point" or method_name == "3":
            solver = FixedPoint()
        elif method_name == "Secant" or method_name == "5":
            solver = Secant()
        elif method_name == "Newton-Raphson" or method_name == "4":
            solver = NewtonRaphson()
        elif method_name == "First modified Newton":
            solver = FirstModifiedNewton()
        elif method_name == "Second modified Newton":
            solver = SecondModifiedNewton()
        elif method_name == "Bierge Vieta" or method_name == "6":
            solver = BiergeVieta()
        # TODO adding general method
        return solver.solve(equation, *args)


solvers = RootFinderFactory()
print(solvers.solve("Bisection", "x ** 2 - 9", 1, 5)[2])
