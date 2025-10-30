from django.contrib import admin
from .models import Car, TestDriveRequest

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price', 'mileage', 'color', 'availability')
    list_filter = ('make', 'year', 'color', 'availability')
    search_fields = ('make', 'model', 'vin', 'license_plate')
    readonly_fields = ('history',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('make', 'model', 'year', 'price', 'mileage', 'color', 'location', 'availability')
        }),
        ('Технические характеристики', {
            'fields': ('engine_size', 'transmission', 'doors', 'fuel_consumption')
        }),
        ('Документы', {
            'fields': ('vin', 'license_plate', 'registration_date')
        }),
        ('Изображение', {
            'fields': ('image',)
        }),
        ('История автомобиля', {
            'fields': ('history',)
        }),
    )

@admin.register(TestDriveRequest)
class TestDriveRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'car', 'date', 'test_drive_price', 'reservation_made_at', 'reservation_cancelled')
    list_filter = ('reservation_cancelled', 'date')
    search_fields = ('name', 'email', 'phone', 'car__make', 'car__model')
    readonly_fields = ('test_drive_price', 'reservation_made_at')
