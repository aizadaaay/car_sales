from django.db import transaction
from .models import Car, TestDriveRequest

def book_test_drive(car_id, name, email, phone, date):
    car = Car.objects.get(id=car_id)

    with transaction.atomic():
        if not car.availability:
            raise Exception("❌ Машина недоступен для тест-драйва.")

        test_drive = TestDriveRequest.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            car=car
        )

        # Машинаның пробегін автоматты 10 км арттырамыз (имитация үшін)
        car.mileage += 10
        car.save()

    return test_drive
