import math

EPSILON = 1e-9

def solve(a: float, b: float, c: float) -> list[float]:
    for value in (a, b, c):
        if not math.isfinite(value):
            raise ValueError("Coefficients must be finite numbers")

    if abs(a) < EPSILON:
        raise ValueError("Coefficient 'a' must not be zero")

    discriminant = b * b - 4 * a * c

    if discriminant < -EPSILON:
        return []

    if abs(discriminant) < EPSILON:
        x = -b / (2 * a)
        return [x]

    sqrt_d = math.sqrt(discriminant)
    x1 = (-b + sqrt_d) / (2 * a)
    x2 = (-b - sqrt_d) / (2 * a)

    return [x1, x2]