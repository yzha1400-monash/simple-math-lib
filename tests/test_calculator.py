import pytest
from src.calculator import add, subtract, divide


# --- 1. 正常路径测试 (Happy Path) ---
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 3) == 7
    assert subtract(0, 5) == -5


def test_divide_normal():
    assert divide(10, 2) == 5.0
    assert divide(3, 2) == 1.5


# --- 2. 边界异常测试 (Edge Case) ---
def test_divide_by_zero_raises_error():
    # 断言：当调用 divide(1, 0) 时，必须抛出 ValueError
    with pytest.raises(ValueError, match="除数不能为零"):
        divide(1, 0)
