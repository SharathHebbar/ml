import mathlib


def test_calc_add():
    total = mathlib.calc_add(4, 5)
    assert total == 9


def test_calc_multiply():
    total = mathlib.calc_multiply(10, 3)
    assert total == 30
