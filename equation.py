from sympy import Symbol, Eq, solve, sin, cos, tan, sec, csc, cot, log, exp, sqrt


def solve_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(expression, 0)
        result = solve(equation, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to solve the equation."
    except NotImplementedError:
        return "Unable to solve the equation. The operation might not be supported."


def solve_sin_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(sin(expression), 0)
        result = solve(equation, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to solve the equation."
    except NotImplementedError:
        return "Unable to solve the equation. The operation might not be supported."


def solve_cos_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(cos(expression), 0)
        result = solve(equation, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to solve the equation."
    except NotImplementedError:
        return "Unable to solve the equation. The operation might not be supported."


def solve_tan_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(tan(expression), 0)
        result = solve(equation, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to solve the equation."
    except NotImplementedError:
        return "Unable to solve the equation. The operation might not be supported."


def solve_sec_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(sec(expression), 0)
        result = solve(equation, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to solve the equation."
    except NotImplementedError:
        return "Unable to solve the equation. The operation might not be supported."


def solve_csc_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(csc(expression), 0)
        result = solve(equation, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to solve the equation."
    except NotImplementedError:
        return "Unable to solve the equation. The operation might not be supported."


def solve_cot_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(cot(expression), 0)
        result = solve(equation, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to solve the equation."
    except NotImplementedError:
        return "Unable to solve the equation. The operation might not be supported."


def solve_exponential_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(exp(expression), 0)
        result = solve(equation, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to solve the equation."
    except NotImplementedError:
        return "Unable to solve the equation. The operation might not be supported."


def solve_logarithm_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(log(expression), 0)
        result = solve(equation, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to solve the equation."
    except NotImplementedError:
        return "Unable to solve the equation. The operation might not be supported."


def solve_sqrt_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(sqrt(expression), 0)
        result = solve(equation, x)
        return result
    except (TypeError, ValueError):
        return "Invalid input or unable to solve the equation."
    except NotImplementedError:
        return "Unable to solve the equation. The operation might not be supported."
