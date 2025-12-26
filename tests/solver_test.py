import math
import pytest
from src.solver import solve

EPSILON = 1e-9

def log_test(message: str):
    """Выводит сообщение о успешном прохождении теста."""

    print(f"\n✅ Тест прошёл: {message}")

def test_no_roots():
    """
    Тест 1: Проверка квадратного уравнения без действительных корней.
    
    Уравнение: 
        x^2 + 1 = 0
    Ожидаемый результат: 
        пустой список.
    """

    result = solve(1.0, 0.0, 1.0)
    assert result == []
    
    log_test("Нет корней для уравнения x^2 + 1 = 0")

def test_two_roots():
    """
    Тест 2: Проверка квадратного уравнения с двумя различными корнями.
    
    Уравнение: 
        x^2 - 1 = 0
    Ожидаемый результат: 
        два корня {1.0, -1.0}.
    """

    roots = solve(1.0, 0.0, -1.0)
    assert set(roots) == {1.0, -1.0}

    log_test("Два корня для уравнения x^2 - 1 = 0 (x=1, x=-1)")

def test_double_root_exact():
    """
    Тест 3: Проверка квадратного уравнения с одним корнем кратности 2.
    
    Уравнение: 
        x^2 + 2x + 1 = 0
    Ожидаемый результат: 
        один корень -1.0.
    """

    roots = solve(1.0, 2.0, 1.0)
    assert len(roots) == 1
    assert abs(roots[0] + 1.0) < EPSILON

    log_test("Один корень кратности 2 для уравнения x^2 + 2x + 1 = 0 (x=-1)")

def test_double_root_with_epsilon():
    """
    Тест 3b: Проверка корня с использованием EPSILON для случая дискриминанта близкого к нулю.
    
    Уравнение: 
        x^2 + 2x + (1 + 1e-12) ≈ 0
    Ожидаемый результат: 
        один корень -1.0.
    """

    a = 1.0
    b = 2.0
    c = 1.0 + 1e-12  # дискриминант < EPSILON

    roots = solve(a, b, c)
    assert len(roots) == 1
    assert abs(roots[0] + 1.0) < EPSILON

    log_test("Один корень через EPSILON для уравнения с D ≈ 0")

def test_a_cannot_be_zero():
    """
    Тест 4: Проверка, что коэффициент 'a' не может быть равен нулю.
    
    Уравнение: 
        0*x^2 + 2x + 1
    Ожидаемый результат: 
        выброс ValueError.
    """

    with pytest.raises(ValueError):
        solve(0.0, 2.0, 1.0)

    log_test("Выброшено исключение при a = 0")

@pytest.mark.parametrize("a,b,c", [
    (math.nan, 1.0, 1.0),
    (1.0, math.nan, 1.0),
    (1.0, 1.0, math.nan),
    (math.inf, 1.0, 1.0),
    (1.0, math.inf, 1.0),
    (1.0, 1.0, math.inf),
])
def test_invalid_double_values(a: float, b: float, c: float):
    """
    Тест 5: Проверка работы функции с некорректными значениями коэффициентов (NaN, ±inf).
    
    Ожидаемый результат: 
        выброс ValueError.
    """

    with pytest.raises(ValueError):
        solve(a, b, c)

    log_test(f"Выброшено исключение при некорректных значениях коэффициентов: a={str(a)}, b={str(b)}, c={str(c)}")