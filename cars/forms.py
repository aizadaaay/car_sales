from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'make', 'model', 'price', 'mileage', 'color', 'engine_size', 'transmission',
            'availability', 'location', 'registration_date', 'vin', 'year', 'doors',
            'license_plate', 'image', 'fuel_consumption', 'history'
        ]
        widgets = {
            'registration_date': forms.DateInput(attrs={'type': 'date'}),
            'availability': forms.Select(choices=[(True, 'В наличии'), (False, 'Продан')]),
        }

from django import forms

class CarPriceForm(forms.Form):
    year = forms.IntegerField(label="Год выпуска")
    mileage = forms.IntegerField(label="Пробег (км)")
    engine_size = forms.FloatField(label="Объем двигателя (л)")
    brand = forms.CharField(label="Марка", max_length=100)
    model = forms.CharField(label="Модель", max_length=100)
    body_type = forms.CharField(label="Кузов", max_length=100)
    transmission = forms.CharField(label="Коробка передач", max_length=100)
    drive = forms.CharField(label="Привод", max_length=100)
    color = forms.CharField(label="Цвет", max_length=100)
    wheel = forms.CharField(label="Руль", max_length=100)
    engine_type = forms.CharField(label="Тип двигателя", max_length=100)
