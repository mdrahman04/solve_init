from sympy import Point, Line, Circle, Polygon, Segment, Triangle, Eq, solve, pi, Symbol


def calculate_distance(point1_coords, point2_coords):
    x1, y1 = point1_coords
    x2, y2 = point2_coords
    try:
        distance = Point(x1, y1).distance(Point(x2, y2))
        return distance
    except (TypeError, ValueError):
        return "Invalid input or unable to calculate distance."


def calculate_slope(point1_coords, point2_coords):
    x1, y1 = point1_coords
    x2, y2 = point2_coords
    try:
        slope = (y2 - y1) / (x2 - x1)
        return slope
    except (TypeError, ZeroDivisionError):
        return "Invalid input or unable to calculate slope."


def calculate_midpoint(point1_coords, point2_coords):
    x1, y1 = point1_coords
    x2, y2 = point2_coords
    try:
        midpoint_x = (x1 + x2) / 2
        midpoint_y = (y1 + y2) / 2
        return midpoint_x, midpoint_y
    except (TypeError, ValueError):
        return "Invalid input or unable to calculate midpoint."


def calculate_circle_area(radius):
    try:
        circle = Circle(Point(0, 0), radius)
        area = circle.area
        return area
    except (TypeError, ValueError):
        return "Invalid input or unable to calculate circle area."


def calculate_triangle_area(vertices_coords):
    vertex1_coords, vertex2_coords, vertex3_coords = vertices_coords
    try:
        triangle = Triangle(Point(*vertex1_coords), Point(*vertex2_coords), Point(*vertex3_coords))
        area = triangle.area
        return area
    except (TypeError, ValueError):
        return "Invalid input or unable to calculate triangle area."


def check_collinear(points_coords):
    try:
        points = [Point(*coords) for coords in points_coords]
        collinear = all(points[0].is_collinear(p) for p in points[1:])
        return collinear
    except (TypeError, ValueError):
        return "Invalid input or unable to check collinearity."


def check_concyclic(points_coords):
    try:
        points = [Point(*coords) for coords in points_coords]
        concyclic = all(points[0].is_concyclic(p) for p in points[1:])
        return concyclic
    except (TypeError, ValueError):
        return "Invalid input or unable to check concyclicity."
