# solve_init

[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](LICENSE)

## about it

solve_init is a comprehensive Python math-solving program that brings together essential and advanced mathematical functions in a single, easily customizable package. Designed to cater to diverse mathematical needs, this program offers a user-friendly interface and powerful mathematical capabilities.

[!! aligned with the intention to make math solving faster in certain cases... !!]

## usage (Sympy)

0. Always use "()" parentheses for avoiding syntax errors. There is no "{}" or square brackets, rather use ((...)).

1. Exponentiation: Instead of using the caret (^) symbol for exponentiation, use the double asterisk (**) operator. For example, x^2 should be written as x**2.

2. Multiplication: Explicitly use the asterisk (*) for multiplication. For example, 2x should be written as 2*x.

3. Function Calls: Use parentheses () when calling functions. For example, to evaluate a trigonometric function, write sin(x) instead of sin x.

4. Fractions: For fractions, use the Sympy Rational class or the / operator. For example, 1/3.

5. Square Roots: To represent square roots, use the sqrt() function. For example, the square root of x should be written as sqrt(x). Or (x)**(1/2) could also be used.

6. Constants: Use the appropriate Sympy constants, such as pi, E, and oo (infinity), instead of manually entering their values.

7. Symbols: Define symbols using the Symbol() function before using them in expressions. For example, x = Symbol('x') declares x as a symbol.

8. Solving Equations: While, using Equation solving functions do not write the right hand sides as "ax+b=0" just write "ax+b". For "ax+b=c" write "ax+b-c".

## functions

~ integration (indefinite)
~ definite integration
~ area by integration (definite)
~ differentiate
~ maclaurins's theorem
~ implicit differentiation
~ limit
~ equations
~ probability
~ distance (lines)
~ circular area
~ calculate slope
~ midpoint (lines)
~ triangular area
~ checking collinear
~ checking concyclic
~ ... to be added

## modifying

the functions provided above can easily be modified depending upon the needs.

1. to add new functions, create a new .py file (e.g., trigonometry.py) in the same directory as app.py. import Sympy and any other necessary functions and define the new process.

2. in app.py, import the defined processes using "from trigonometry.py import ..." and link them to the index.html and other functions using app routes.

3. in index.html, add the new form and input fields specific to the new function, and include a new button defining its action.

## things to develop

1. more complex problem solving functions.

2. steps interpreter.

3. keeping it fully accessible over a all kind of devices, specifically over old non-touch devices.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0). You are free to use, modify, and distribute it within the license terms.

## Contact

For any inquiries, suggestions, or support, feel free to reach out:

- GitHub: [@mdrahman04] (https://github.com/mdrahman04)

Your feedback and contributions are greatly appreciated. Together, let's enhance the world of mathematics with solve_init!
