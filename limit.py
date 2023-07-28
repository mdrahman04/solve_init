def calculate_limit(expression, variable, value):
    try:
        # Import required modules (you may need to install sympy)
        from sympy import limit, Symbol, sympify

        # Convert the expression to a sympy expression
        expr = sympify(expression)

        # Define the variable as a sympy symbol
        x = Symbol(variable)

        # Calculate the limit and return the result
        result = limit(expr, x, value)
        return result

    except Exception as e:
        return str(e)  # Return an error message if there's an issue with the input
