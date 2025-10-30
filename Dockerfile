# Используем официальное изображение Python 3.12.6
FROM python:3.12.6-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt .

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в контейнер
COPY . .

# Выполняем сборку статических файлов Django
RUN python manage.py collectstatic --noinput

# Выполняем миграции базы данных
RUN python manage.py migrate

# Настраиваем порт для Render
ENV PORT 10000

# Запуск Django через Gunicorn
CMD ["gunicorn", "car_sales.wsgi:application", "--bind", "0.0.0.0:10000"]
