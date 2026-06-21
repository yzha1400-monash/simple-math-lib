# Simple-Math-Lib

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)

一个用于学习软件工程基础的小型计算库，包含加、减、除功能。

## 快速开始

安装依赖：

```bash
pip install -r requirements.txt
使用示例：

python
from src.calculator import add, divide

print(add(10, 20))
print(divide(9, 3))
运行测试
bash
python -m pytest -v
许可证
MIT

text

---

### 📄 同样，`docs/usage.md` 的绝对正确内容也给你（请全选复制）：

```markdown
# 使用手册

## API 参考

### add(a, b)
返回两个数字的和。

### subtract(a, b)
返回第一个数字减去第二个数字的差。

### divide(a, b)
返回两个数字的商。
如果除数为 0，则会抛出 ValueError 异常。