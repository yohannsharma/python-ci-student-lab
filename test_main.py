from main import add


def test_add():
    assert add(3, 2) == 5


def test_add_zero():
    assert add(7, 0) == 7


def test_add_negative_numbers():
    assert add(-3, -2) == -5


def test_add_mixed_signs():
    assert add(-3, 2) == -1
