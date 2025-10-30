from django.shortcuts import render
from .models import Car

def home(request):
    cars = Car.objects.all().order_by('-id')[:4]  # Берем последние 4 машины
    for car in cars:
        if not car.image:
            car.image = 'default_image.jpg'  # Путь к изображению по умолчанию
    return render(request, 'cars/home.html', {'cars': cars})


# views.py
from django.shortcuts import render
from .models import Car

def car_list(request):
    # Получаем параметры фильтра из GET-запроса
    make = request.GET.get('make', '')
    year_min = request.GET.get('year_min', '')
    year_max = request.GET.get('year_max', '')
    price_min = request.GET.get('price_min', '')
    price_max = request.GET.get('price_max', '')
    engine_min = request.GET.get('engine_min', '')
    engine_max = request.GET.get('engine_max', '')

    # Начинаем с базового запроса ко всем автомобилям
    cars = Car.objects.all()

    # Фильтрация по марке
    if make:
        cars = cars.filter(make__icontains=make)

    # Фильтрация по диапазону года выпуска
    if year_min:
        try:
            year_min = int(year_min)
            cars = cars.filter(year__gte=year_min)
        except ValueError:
            pass  # Игнорируем, если year_min не является числом
    if year_max:
        try:
            year_max = int(year_max)
            cars = cars.filter(year__lte=year_max)
        except ValueError:
            pass  # Игнорируем, если year_max не является числом

    # Фильтрация по диапазону цены
    if price_min:
        try:
            price_min = float(price_min)
            cars = cars.filter(price__gte=price_min)
        except ValueError:
            pass  # Игнорируем, если price_min не является числом
    if price_max:
        try:
            price_max = float(price_max)
            cars = cars.filter(price__lte=price_max)
        except ValueError:
            pass  # Игнорируем, если price_max не является числом

    # Фильтрация по диапазону объема двигателя
    if engine_min:
        try:
            engine_min = float(engine_min)
            cars = cars.filter(engine_size__gte=engine_min)
        except ValueError:
            pass  # Игнорируем, если engine_min не является числом
    if engine_max:
        try:
            engine_max = float(engine_max)
            cars = cars.filter(engine_size__lte=engine_max)
        except ValueError:
            pass  # Игнорируем, если engine_max не является числом

    return render(request, 'cars/car_list.html', {'cars': cars})
 

from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Car
from .forms import CarForm
from decimal import Decimal

def add_car(request):
    # 🔹 Последние 5 автомобилей
    last_cars = list(Car.objects.order_by('-id')[:5])
    recommended_cars = None
    message = None
    selected_car = None

    # 🔹 Получаем ID из формы (выпадающий список или ручной ввод)
    car_id = request.GET.get('car_id') or request.GET.get('car_id_manual')

    if car_id:
        try:
            # Проверяем, что ID — число
            car_id = int(car_id)
            selected_car = get_object_or_404(Car, id=car_id)

            # ✅ Если выбранная машина не в списке последних — добавляем её в конец
            if selected_car not in last_cars:
                last_cars.append(selected_car)

            # 🔹 Подбор похожих машин по цене ±10% и цвету/марке
            price_min = selected_car.price * Decimal('0.9')
            price_max = selected_car.price * Decimal('1.1')

            recommended_cars = Car.objects.filter(
                Q(make=selected_car.make) | Q(color=selected_car.color),
                price__gte=price_min,
                price__lte=price_max
            ).exclude(id=selected_car.id)[:5]

        except ValueError:
            message = f"❌ Введённый ID «{car_id}» не является числом."
        except Car.DoesNotExist:
            message = f"❌ Машина с ID {car_id} не найдена."

    # 🔹 Добавление нового автомобиля
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            new_car = form.save()
            message = f"✅ Автомобиль {new_car.make} {new_car.model} успешно добавлен!"
            return render(request, 'cars/add_car.html', {
                'form': CarForm(),
                'last_cars': last_cars,
                'message': message,
                'selected_car': new_car,
            })
    else:
        form = CarForm()

    # 🔹 Рендер шаблона
    return render(request, 'cars/add_car.html', {
        'form': form,
        'last_cars': last_cars,
        'recommended_cars': recommended_cars,
        'selected_car': selected_car,
        'message': message,
    })





from django.shortcuts import render, get_object_or_404
from .models import Car
from .forms import CarForm
from django.http import HttpResponse

def credit_calculator(request):
    return render(request, 'cars/credit_calculator.html')  # Убедитесь, что путь правильный
from django.shortcuts import render

def about(request):
    return render(request, 'cars/about.html')
def contact(request):
    return render(request, 'cars/contact.html')  # Убедитесь, что путь правильный

from django.shortcuts import render
from .models import Car
from django.shortcuts import render
from .models import Car


from django.shortcuts import render, get_object_or_404
from .models import Car  # или ваша модель автомобилей
from .utils import calculate_maintenance_costs  # Импортируем функцию для расчетов


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    
    testdriverequest = TestDriveRequest.objects.filter(
        car=car,
        reservation_cancelled=False
    ).order_by('-reservation_made_at').first()

    costs = None
    message = None
    test_drive_price = None

    if testdriverequest:
        expired = testdriverequest.check_reservation_expiration()
        if expired:
            message = "Бронь на тест-драйв снята. Машина снова доступна."
        elif testdriverequest.reservation_cancelled:
            message = "Бронь на тест-драйв уже была отменена."
        test_drive_price = testdriverequest.test_drive_price
    else:
        # Если тест-драйвов нет, считаем цену на основе машины
        test_drive_price = 5000 + (car.engine_size * 1000)

    if request.method == 'POST':
        fuel_consumption = float(request.POST.get('fuel_consumption'))
        fuel_price = float(request.POST.get('fuel_price'))
        distance_per_year = int(request.POST.get('distance_per_year'))
        tax_rate = car.engine_size * 10
        insurance_rate = car.engine_size * 20

        costs = calculate_maintenance_costs(
            fuel_consumption, fuel_price, distance_per_year, tax_rate, insurance_rate
        )

    return render(
        request,
        'cars/car_detail.html',
        {
            'car': car,
            'costs': costs,
            'testdriverequest': testdriverequest,
            'message': message,
            'test_drive_price': test_drive_price,
        }
    )

from django.contrib import messages



def credit_calculator(request):
    return render(request, 'cars/credit_calculator.html')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Car, TestDriveRequest
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Car, TestDriveRequest

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Car, TestDriveRequest

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Car
from .services import book_test_drive  # 📌 Қосуды ұмытпаңыз!

def test_drive(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')

        # 📢 book_test_drive арқылы брондау
        try:
            book_test_drive(car_id, name, email, phone, date)
        except Exception as e:
            # Машина қолжетімді болмаса немесе басқа қате болса
            return render(request, 'cars/test_drive.html', {
                'car': car,
                'error': str(e)
            })

        return HttpResponseRedirect(reverse('test_drive', args=[car_id]) + '?success=1')

    # Егер URL-да success=1 болса, онда сәтті хабарламаны көрсетеміз
    success = request.GET.get('success') == '1'

    return render(request, 'cars/test_drive.html', {
        'car': car,
        'success': success
    })



# cars/views.py
from django.shortcuts import render
from .utils import calculate_maintenance_costs, compare_cars
from .models import Car

def maintenance_cost_view(request):
    if request.method == "POST":
        fuel_consumption = float(request.POST['fuel_consumption'])
        fuel_price = float(request.POST['fuel_price'])
        distance_per_year = float(request.POST['distance_per_year'])
        tax_rate = float(request.POST['tax_rate'])
        insurance_rate = float(request.POST['insurance_rate'])
        costs = calculate_maintenance_costs(fuel_consumption, fuel_price, distance_per_year, tax_rate, insurance_rate)
        return render(request, 'cars/maintenance_result.html', {'costs': costs})
    return render(request, 'cars/maintenance_calculator.html')

def car_comparison_view(request):
    selected_car_ids = request.POST.getlist('selected_cars')
    cars = Car.objects.filter(id__in=selected_car_ids)
    comparison_table = compare_cars(cars)  # ⚠️ ВАЖНО: что возвращает эта функция?
    return render(request, 'cars/car_comparison.html', {'comparison_table': comparison_table, 'cars': cars})


from django.shortcuts import render
from .utils import calculate_maintenance_costs  # Импортируем функцию для расчетов

def maintenance_cost_view(request, car_id):
    car = Car.objects.get(id=car_id)  # Получаем машину по ID, если необходимо
    costs = None

    if request.method == "POST":
        # Получаем данные из формы
        fuel_consumption = float(request.POST.get('fuel_consumption'))
        fuel_price = float(request.POST.get('fuel_price'))
        distance_per_year = int(request.POST.get('distance_per_year'))

        # Выполняем расчет
        costs = calculate_maintenance_costs(fuel_consumption, fuel_price, distance_per_year, car.tax_rate, car.insurance_rate)

    return render(request, 'cars/maintenance_result.html', {'costs': costs})


from django.shortcuts import render
from django.http import JsonResponse
from .ml_model import predict_price, model





import pickle
import os
import numpy as np
from django.shortcuts import render
from .forms import CarPriceForm

# Путь к моделям
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "car_price_model.pkl")
PREPROCESSOR_PATH = os.path.join(BASE_DIR, "preprocessor.pkl")

# Загрузка модели
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# Загрузка предобработчика
with open(PREPROCESSOR_PATH, "rb") as f:
    preprocessor = pickle.load(f)

def predict_price(request):
    predicted_price = None

    if request.method == "POST":
        form = CarPriceForm(request.POST)
        if form.is_valid():
            data = [
                form.cleaned_data["year"],
                form.cleaned_data["mileage"],
                form.cleaned_data["engine_size"],
                form.cleaned_data["brand"],
                form.cleaned_data["model"],
                form.cleaned_data["body_type"],
                form.cleaned_data["transmission"],
                form.cleaned_data["drive"],
                form.cleaned_data["color"],
                form.cleaned_data["wheel"],
                form.cleaned_data["engine_type"],
            ]

            # Преобразуем в DataFrame
            import pandas as pd
            columns = ['Год выпуска', 'Пробег', 'Объем двигателя, л (число)',
                       'Марка', 'Модель', 'Кузов', 'Коробка передач',
                       'Привод', 'Цвет', 'Руль', 'Объем двигателя, л (тип)']
            input_df = pd.DataFrame([data], columns=columns)

            # Преобразуем данные с помощью preprocessor
            X_input = preprocessor.transform(input_df)

            # Предсказание
            y_pred_log = model.predict(X_input)
            predicted_price = np.expm1(y_pred_log)[0]  # Обратное логарифмирование

    else:
        form = CarPriceForm()

    return render(request, "cars/predict_form.html", {"form": form, "predicted_price": predicted_price})
