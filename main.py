def greeting():
    return "Hello, welcome to the Anthropic API course!"


def calculate_pi(num_terms: int = 1000000) -> float:
    """Calculate pi using the Leibniz formula:
    pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...
    """
    pi = 0.0
    for i in range(num_terms):
        pi += ((-1) ** i) / (2 * i + 1)
    return pi * 4