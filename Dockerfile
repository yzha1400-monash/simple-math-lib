# 1. 使用官方 Python 轻量级镜像作为基础
FROM python:3.10-slim

# 2. 设置工作目录（容器里的默认路径）
WORKDIR /app

# 3. 先拷贝依赖文件（利用 Docker 缓存层，节省构建时间）
COPY requirements.txt .

# 4. 安装依赖（换国内清华源，避免网络超时）
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 5. 拷贝项目源码和测试代码
COPY src/ ./src/
COPY tests/ ./tests/

# 6. 设置 Python 路径，确保能找到 src 包
ENV PYTHONPATH=/app

# 7. 默认启动命令：运行单元测试（验证容器环境是否健康）
#    这样你每次构建镜像后，运行容器就能直接看到测试结果
CMD ["pytest", "-v"]