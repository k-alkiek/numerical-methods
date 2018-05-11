from src.roots_finder.bracketing_methods.bisection import Bisection
from src.roots_finder.bracketing_methods.regula_falsi import FalsePosition
from src.roots_finder.open_methods.fixed_point import FixedPoint
from src.roots_finder.open_methods.secant import Secant
from src.roots_finder.open_methods.Newton_Raphson import NewtonRaphson
from src.roots_finder.open_methods.first_modified_Newton import FirstModifiedNewton
from src.roots_finder.open_methods.second_modified_Newton import SecondModifiedNewton
from src.roots_finder.roots_of_polynomial.Bierge_Vieta import BiergeVieta
from controllers import bracketing_methods_controller, fixed_point_controller, \
    newton_raphson_controller, birge_vieta_controller, secant_controller


class RootFinderFactory:
    def solve(self, method_name, equation, *args):
        solver = None
        PlotWindow = None
        DataTable = None
        if method_name == "Bisection" or method_name == "1":
            solver = Bisection()
            PlotWindow = bracketing_methods_controller.PlotWindow
            DataTable = bracketing_methods_controller.DataTable
        elif method_name == "False Position" or method_name == "2":
            solver = FalsePosition()
            PlotWindow = bracketing_methods_controller.PlotWindow
            DataTable = bracketing_methods_controller.DataTable
        elif method_name == "Fixed Point" or method_name == "3":
            solver = FixedPoint()
            PlotWindow = fixed_point_controller.PlotWindow
            DataTable = fixed_point_controller.DataTable
        elif method_name == "Secant" or method_name == "5":
            solver = Secant()
            PlotWindow = secant_controller.PlotWindow
            DataTable = secant_controller.DataTable
        elif method_name == "Newton-Raphson" or method_name == "4":
            solver = NewtonRaphson()
            PlotWindow = newton_raphson_controller.PlotWindow
            DataTable = newton_raphson_controller.DataTable
        elif method_name == "First modified Newton":
            solver = FirstModifiedNewton()
            PlotWindow = newton_raphson_controller.PlotWindow
            DataTable = newton_raphson_controller.DataTable
        elif method_name == "Second modified Newton":
            solver = SecondModifiedNewton()
            PlotWindow = newton_raphson_controller.PlotWindow
            DataTable = newton_raphson_controller.DataTable
        elif method_name == "Birge Vieta" or method_name == "6":
            solver = BiergeVieta()
            PlotWindow = birge_vieta_controller.PlotWindow
            DataTable = birge_vieta_controller.DataTable
        # TODO adding general method
        return solver.solve(equation, *args), PlotWindow, DataTable


solvers = RootFinderFactory()
