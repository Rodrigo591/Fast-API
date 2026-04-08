@echo off
docker-compose down
docker-compose build --no-cache
start cmd /k docker-compose up
timeout /t 10
start http://localhost:8000/docs