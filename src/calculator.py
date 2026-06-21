"""
calculator.py: 四则运算核心 API 模块
此模块提供基础的数学运算功能。
"""


def add(a: float, b: float) -> float:
    """返回两个数字的和。"""
    return a + b


def subtract(a: float, b: float) -> float:
    """返回第一个数字减去第二个数字的差。"""
    return a - b


def divide(a: float, b: float) -> float:
    """
    执行除法运算，若除数为 0 则抛出 ValueError。

    Args:
        a: 被除数
        b: 除数

    Returns:
        浮点数商

    Raises:
        ValueError: 当 b == 0 时触发
    """
    if b == 0:
        raise ValueError("除数不能为零，请传入非零数值。")
    return a / b
