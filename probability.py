from sympy import Symbol


def calculate_probability(event_outcomes, total_outcomes):
    try:
        probability = event_outcomes / total_outcomes
        return probability
    except (TypeError, ValueError, ZeroDivisionError):
        return "Invalid input or unable to calculate probability."


def calculate_conditional_probability(event_outcomes_a, total_outcomes_a, event_outcomes_b, total_outcomes_b):
    try:
        probability_a = event_outcomes_a / total_outcomes_a
        probability_b_given_a = event_outcomes_b / total_outcomes_a
        conditional_probability = probability_b_given_a * probability_a
        return conditional_probability
    except (TypeError, ValueError, ZeroDivisionError):
        return "Invalid input or unable to calculate conditional probability."
