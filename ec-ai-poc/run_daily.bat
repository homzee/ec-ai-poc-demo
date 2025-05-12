@echo off
REM 进入容器并运行 trigger
curl -X POST http://localhost:8000/trigger
