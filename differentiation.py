from sympy import Symbol, diff, sin, cos, tan, sec, csc, cot, log, exp, sqrt, Eq, solve, symbols, sympify
from sympy.series import series


def differentiate_function(expression, variable):
    x = Symbol(variable)
    try:
        result = diff(expression, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to differentiate the expression."
    except NotImplementedError:
        return "Unable to differentiate the expression. The operation might not be supported."


def explicit_differentiate(expression, variable):
    x = symbols(variable)
    expr = sympify(expression)
    derivative = diff(expr, x)
    return derivative


def implicit_differentiate(expression, variable):
    x, y = symbols(variable, 'y')
    expr = sympify(expression)
    eq = Eq(expr, 0)
    dy_dx = solve(eq.diff(x), diff(y, x))
    return dy_dx


def maclaurin_theorem(expression, variable, order):
    x = symbols(variable)
    expr = sympify(expression)
    series_result = series(expr, x, 0, order)
    return series_result.removeO()
