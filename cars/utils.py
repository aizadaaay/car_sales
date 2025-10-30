# cars/utils.py

def calculate_maintenance_costs(fuel_consumption, fuel_price, distance_per_year, tax_rate, insurance_rate):
    fuel_costs = (distance_per_year / 100) * fuel_consumption * fuel_price
    total_cost = fuel_costs + tax_rate + insurance_rate
    return {
    "fuel_costs": round(fuel_costs, 2),
    "tax": tax_rate,
    "insurance": insurance_rate,
    "total_cost": round(total_cost, 2)
}


def compare_cars(cars):
    comparison_table = []

    for car in cars:
        comparison_table.append({
            "Марка": car.make,
            "Модель": car.model,
            "Цена": car.price,
            "Пробег": car.mileage,
            "Расход топлива": car.fuel_consumption
        })
    return comparison_table
