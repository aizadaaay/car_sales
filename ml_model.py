import pickle
import numpy as np

# Загружаем сохраненную модель и предобработчик
with open("cars/prediction_pipeline.pkl", "rb") as file:
    preprocessor, model = pickle.load(file)

def predict_price(features):
    """
    Принимает словарь с характеристиками автомобиля и возвращает предсказанную цену.
    """
    try:
        # Преобразуем входные данные в формат numpy массива
        num_features = ['Год выпуска', 'Пробег', 'Объем двигателя, л (число)']
        cat_features = ['Марка', 'Модель', 'Кузов', 'Коробка передач', 'Привод', 'Цвет', 'Руль', 'Объем двигателя, л (тип)']

        # Разделение на числовые и категориальные признаки
        num_values = [float(features[key]) for key in num_features]
        cat_values = [features[key] for key in cat_features]

        # Объединяем данные в единую строку для предсказания
        input_data = np.array(num_values + cat_values, dtype=object).reshape(1, -1)

        # Применяем предобработку
        transformed_data = preprocessor.transform(input_data)

        # Делаем предсказание
        predicted_log_price = model.predict(transformed_data)[0]
        predicted_price = np.expm1(predicted_log_price)  # Обратное логарифмирование

        return round(predicted_price, 2)
    except Exception as e:
        return str(e)  # Вернем ошибку
