from setuptools import setup, find_packages

setup(
    name="simple-math-lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # 依赖由 requirements.txt 管理
    python_requires=">=3.8",
)