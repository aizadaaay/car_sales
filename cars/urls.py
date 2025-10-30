from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('cars/', views.car_list, name='car_list'),  # Список автомобилей
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),  # Детальная информация о машине
    path('add/', views.add_car, name='add_car'),  # Страница добавления автомобиля
    path('credit-calculator/', views.credit_calculator, name='credit_calculator'),  # Калькулятор кредита
    path('about/', views.about, name='about'),  # О нас
    path('contact/', views.contact, name='contact'),
    path('add_car/', views.add_car, name='add_car'),
    path('add/', views.add_car, name='add_car'),  # Путь для добавления автомобиля
    path('test-drive/<int:car_id>/', views.test_drive, name='test_drive'),# Контакты
    path('maintenance/', views.maintenance_cost_view, name='maintenance_cost'),
    path('compare/', views.car_comparison_view, name='car_comparison'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('prediction/', views.predict_price, name='prediction'),

]
