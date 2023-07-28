from flask import Flask, render_template, request
from sympy import Symbol, diff, Eq, solve, sympify
from sympy.core.sympify import SympifyError
from sympy.geometry import Point, Circle
from limit import calculate_limit
from differentiation import implicit_differentiate, maclaurin_theorem
from integration import indefinite_integration, definite_integration, area_by_definite_integration

app = Flask(__name__)

# Math Functions


def differentiate_expression(expression, variable):
    x = Symbol(variable)
    result = diff(expression, x)
    return result


def calculate_probability(probability_space, event):
    probability = event / probability_space
    return probability


def calculate_distance(point1, point2):
    distance = point1.distance(point2)
    return distance


def calculate_area_of_circle(radius):
    circle = Circle(Point(0, 0), radius)
    area = circle.area
    return area


def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope


def calculate_midpoint(x1, y1, x2, y2):
    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2
    return midpoint_x, midpoint_y


def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    area = abs(0.5 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
    return area


def check_collinear(x1, y1, x2, y2, x3, y3):
    collinear = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0
    return collinear


def check_concyclic(x1, y1, x2, y2, x3, y3):
    concyclic = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0
    return not concyclic


def solve_equation(expression, variable):
    x = Symbol(variable)
    try:
        equation = Eq(sympify(expression), 0)
        result = solve(equation, x)
        return result[0]
    except SympifyError:
        return "Invalid input: Please provide a valid equation."


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/calculate_indefinite_integration", methods=["POST"])
def calculate_indefinite_integration():
    expression = request.form["expression"]
    variable = request.form["variable"]
    result = indefinite_integration(expression, variable)
    return render_template("index.html", result=result)


@app.route("/calculate_definite_integration", methods=["POST"])
def calculate_definite_integration():
    expression = request.form["expression"]
    variable = request.form["variable"]
    lower_limit = float(request.form["lower_limit"])
    upper_limit = float(request.form["upper_limit"])
    result = definite_integration(expression, variable, lower_limit, upper_limit)
    return render_template("index.html", result=result)


@app.route("/calculate_area_by_definite_integration", methods=["POST"])
def calculate_area_by_definite_integration():
    expression = request.form["expression"]
    variable = request.form["variable"]
    lower_limit = float(request.form["lower_limit"])
    upper_limit = float(request.form["upper_limit"])
    result = area_by_definite_integration(expression, variable, lower_limit, upper_limit)
    return render_template("index.html", result=result)


@app.route('/differentiate', methods=['POST'])
def differentiate():
    expression = request.form['expression']
    variable = request.form['variable']
    result = differentiate_expression(expression, variable)
    return render_template('index.html', result=result, category='Differentiation')


@app.route('/equation', methods=['POST'])
def equation():
    expression = request.form['expression']
    variable = request.form['variable']
    result = solve_equation(expression, variable)
    return render_template('index.html', result=result, category='Equation')


@app.route('/probability', methods=['POST'])
def probability():
    probability_space = float(request.form['probability_space'])
    event = float(request.form['event'])
    result = calculate_probability(probability_space, event)
    return render_template('index.html', result=result, category='Probability')


@app.route('/distance', methods=['POST'])
def distance():
    x1 = float(request.form['x1'])
    y1 = float(request.form['y1'])
    x2 = float(request.form['x2'])
    y2 = float(request.form['y2'])
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    result = calculate_distance(point1, point2)
    return render_template('index.html', result=result, category='Geometry')


@app.route('/circle_area', methods=['POST'])
def circle_area():
    radius = float(request.form['radius'])
    result = calculate_area_of_circle(radius)
    return render_template('index.html', result=result, category='Geometry')


@app.route('/slope', methods=['POST'])
def slope():
    x1 = float(request.form['x1'])
    y1 = float(request.form['y1'])
    x2 = float(request.form['x2'])
    y2 = float(request.form['y2'])
    result = calculate_slope(x1, y1, x2, y2)
    return render_template('index.html', result=result, category='Slope')


@app.route('/midpoint', methods=['POST'])
def midpoint():
    x1 = float(request.form['x1'])
    y1 = float(request.form['y1'])
    x2 = float(request.form['x2'])
    y2 = float(request.form['y2'])
    result = calculate_midpoint(x1, y1, x2, y2)
    return render_template('index.html', result=result, category='Midpoint')


@app.route('/triangle_area', methods=['POST'])
def triangle_area():
    x1 = float(request.form['x1'])
    y1 = float(request.form['y1'])
    x2 = float(request.form['x2'])
    y2 = float(request.form['y2'])
    x3 = float(request.form['x3'])
    y3 = float(request.form['y3'])
    result = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
    return render_template('index.html', result=result, category='Triangle Area')


@app.route('/collinear', methods=['POST'])
def collinear():
    x1 = float(request.form['x1'])
    y1 = float(request.form['y1'])
    x2 = float(request.form['x2'])
    y2 = float(request.form['y2'])
    x3 = float(request.form['x3'])
    y3 = float(request.form['y3'])
    result = check_collinear(x1, y1, x2, y2, x3, y3)
    return render_template('index.html', result=result, category='Collinear')


@app.route('/concyclic', methods=['POST'])
def concyclic():
    x1 = float(request.form['x1'])
    y1 = float(request.form['y1'])
    x2 = float(request.form['x2'])
    y2 = float(request.form['y2'])
    x3 = float(request.form['x3'])
    y3 = float(request.form['y3'])
    result = check_concyclic(x1, y1, x2, y2, x3, y3)
    return render_template('index.html', result=result, category='Concyclic')


@app.route('/limit', methods=['POST'])
def limit_calculation():
    try:
        # Get data from the form submitted by the user
        expression = request.form['expression']
        variable = request.form['variable']
        value = float(request.form['value'])  # Assuming the user provides a numerical value for the limit

        # Calculate the limit using the calculate_limit function from limit.py
        result = calculate_limit(expression, variable, value)

        # Return the result to the frontend
        return render_template('index.html', result=result, category='Limit')

    except Exception as e:
        error_message = "Error: " + str(e)
        return render_template('index.html', error=error_message)


@app.route('/implicit-differentiate', methods=['POST'])
def implicit_differentiate_calculation():
    try:
        # Get data from the form submitted by the user
        expression = request.form['expression']
        variable = request.form['variable']

        # Calculate the derivative
        result = implicit_differentiate(expression, variable)

        # Return the result to the frontend
        return render_template('index.html', result=result, category='Implicit Derivative')

    except Exception as e:
        error_message = "Error: " + str(e)
        return render_template('index.html', error=error_message)


@app.route('/maclaurin-theorem', methods=['POST'])
def maclaurin_theorem_calculation():
    try:
        # Get data from the form submitted by the user
        expression = request.form['expression']
        variable = request.form['variable']
        order = int(request.form['order'])

        # Calculate the Maclaurin's Theorem using the maclaurin_theorem function from differentiate.py
        result = maclaurin_theorem(expression, variable, order)

        # Return the result to the frontend
        return render_template('index.html', result=result, category='Maclaurin\'s Theorem')

    except Exception as e:
        error_message = "Error: " + str(e)
        return render_template('index.html', error=error_message)


if __name__ == '__main__':
    app.run(debug=True)
