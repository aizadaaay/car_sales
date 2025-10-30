# Car Sales

Сайт для продажи автомобилей. Пользователи могут просматривать каталог автомобилей, добавлять новые машины, видеть популярные модели и использовать кредитный калькулятор. 🌐 Доступен онлайн: https://car-sales-qps2.onrender.com/

Основные функции: просмотр каталога автомобилей с фотографиями, фильтрация и сортировка по марке, цене, году и другим параметрам, добавление новых автомобилей с фото и описанием, прогноз цены автомобиля на основе модели машинного обучения, кредитный калькулятор для расчета ежемесячного платежа, информационные страницы "О нас" и "Контакты". Медиа файлы (изображения авто) хранятся на Cloudinary.

Используемые технологии: Django 4.2+, Python 3.12, PostgreSQL, Cloudinary для хранения медиа файлов, HTML, CSS, JavaScript, Gunicorn для продакшн-сервера.

## Установка локально

Клонируем репозиторий и переходим в папку проекта:
git clone https://github.com/aizadaaay/car_sales.git
cd car_sales

Копировать код

Создаем и активируем виртуальное окружение:
python -m venv venv

Linux/macOS
source venv/bin/activate

Windows
venv\Scripts\activate

Копировать код

Устанавливаем зависимости:
pip install -r requirements.txt

go
Копировать код

Настраиваем базу данных PostgreSQL в `settings.py` или через `.env`:
DATABASES = {
'default': dj_database_url.config(
default='postgresql://USERNAME:PASSWORD@HOST:PORT/DBNAME',
conn_max_age=600,
ssl_require=True
)
}

Копировать код

Настраиваем Cloudinary для хранения медиа файлов:
CLOUDINARY_STORAGE = {
'CLOUD_NAME': 'ваш_cloud_name',
'API_KEY': 'ваш_api_key',
'API_SECRET': 'ваш_api_secret',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/' # для совместимости

Копировать код

Применяем миграции:
python manage.py migrate

Копировать код

Создаем суперпользователя:
python manage.py createsuperuser

Копировать код

Запускаем сервер разработки:
python manage.py runserver

cpp
Копировать код

Сайт будет доступен по адресу: http://127.0.0.1:8000/
