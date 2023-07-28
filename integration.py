from sympy import Symbol, integrate, simplify, asin, sqrt


def indefinite_integration(expression, variable):
    x = Symbol(variable)
    integral = integrate(expression, x)
    simplified_integral = simplify(integral)
    return simplified_integral


def definite_integration(expression, variable, lower_limit, upper_limit):
    x = Symbol(variable)
    integral = integrate(expression, (x, lower_limit, upper_limit))
    simplified_integral = simplify(integral)
    return simplified_integral


def area_by_definite_integration(expression, variable, lower_limit, upper_limit):
    x = Symbol(variable)
    integral = integrate(expression, x)  # Find the indefinite integral (antiderivative)
    result_lower = integral.subs(x, lower_limit)  # Evaluate at lower limit
    result_upper = integral.subs(x, upper_limit)  # Evaluate at upper limit
    area = abs(result_upper - result_lower)  # Calculate absolute difference
    return area.evalf()  # Evaluate the result numerically
