
# 基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下所有文件
COPY . .

# 安装依赖
RUN pip install --no-cache-dir \
    fastapi uvicorn python-dotenv requests \
    pandas openai gspread oauth2client \
    google-auth google-auth-oauthlib google-api-python-client



# 启动命令
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

