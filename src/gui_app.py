import sys
import os
import tkinter as tk
from tkinter import messagebox

# 注意：这里的路径处理会在 main 块里动态添加，而不是在模块顶层
from src.calculator import add, divide


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        root.title("极简计算器 GUI")

        tk.Label(root, text="数字 A:").grid(row=0, column=0)
        self.entry_a = tk.Entry(root)
        self.entry_a.grid(row=0, column=1)

        tk.Label(root, text="数字 B:").grid(row=1, column=0)
        self.entry_b = tk.Entry(root)
        self.entry_b.grid(row=1, column=1)

        tk.Button(root, text="相加 (+)", command=self.do_add).grid(row=2, column=0)
        tk.Button(root, text="相除 (/)", command=self.do_divide).grid(row=2, column=1)

        self.result_label = tk.Label(root, text="结果: ")
        self.result_label.grid(row=3, column=0, columnspan=2)

    def do_add(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            result = add(a, b)
            self.result_label.config(text=f"结果: {result}")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的数字")

    def do_divide(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            result = divide(a, b)
            self.result_label.config(text=f"结果: {result}")
        except ValueError as e:
            messagebox.showerror("数学错误", str(e))


if __name__ == "__main__":
    # 只有在直接运行脚本时，才把项目根目录加入 Python 路径
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
    