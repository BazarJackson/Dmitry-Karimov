# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем файлы приложения
COPY calculate.py .

# Задаем переменную окружения для Flask
ENV FLASK_APP=calculate.py
ENV FLASK_RUN_HOST=0.0.0.0

# Открываем порт для Flask
EXPOSE 5000

# Запускаем приложение
CMD ["python", "calculate.py"]
