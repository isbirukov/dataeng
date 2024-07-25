###########################
#### Итоговое задание №3
###########################

#### Что можно было бы доделать
# - объединить функции total_sales_per_product и sales_over_time,
#       т.к. делают, по сути, одно и тоже, но по заданию надо было их реализовать.
# - довести графики до ума, сделать более презентабельными

import matplotlib.pyplot as plt
# Путь до файла
file_path = 'sales.csv'

def read_sales_data(path):
    '''
    Функция открывает файл и возвращает список продаж в виде словарей
    :param path: путь до файла
    :return: список, состоящий из словарей продаж
    '''
    lst = []
    with open(path, encoding='UTF-8') as file:
        for line in file:
            dct = {}
            product_name, quantity, price, date = line.strip().split(", ")
            dct['product_name'] = product_name
            dct['quantity'] = int(quantity)
            dct['price'] = int(price)
            dct['date'] = date
            lst.append(dct)
    return lst

def total_sales_per_product(sales_data):
    '''
    Функция формирует словарь, , где ключ - название продукта,
            а значение - общая сумма продаж этого продукта.
    :param sales_data: список, содержашщий словари продаж
    :return: словарь с общими суммами продаж по продуктам
    '''
    dct_total_sales = {}
    for sale in sales_data:
        if sale['product_name'] in dct_total_sales:
            dct_total_sales[sale['product_name']] += sale['price'] * sale['quantity']
        else:
            dct_total_sales[sale['product_name']] = sale['price'] * sale['quantity']
    return dct_total_sales

def sales_over_time(sales_data):
    '''
    Функция формирует словарь, где ключ - дата, а значение общая сумма продаж за эту дату.
    :param sales_data: список, содержашщий словари продаж
    :return: словарь с общими суммами продаж по датам
    '''
    dct_sales_over_time = {}
    for sale in sales_data:
        if sale['date'] in dct_sales_over_time:
            dct_sales_over_time[sale['date']] += sale['price'] * sale['quantity']
        else:
            dct_sales_over_time[sale['date']] = sale['price'] * sale['quantity']
    return dct_sales_over_time


# формируем список словарей продаж из файла
sales = read_sales_data(file_path)
# сумма продаж по продукту
total_sales_products = total_sales_per_product(sales)
max_product = sorted(total_sales_products.items(), key=lambda x: x[1])[-1]
# сумма продаж по дате
total_sales_over_time = sales_over_time(sales)
max_day_sales = sorted(total_sales_over_time.items(), key=lambda x: x[1])[-1]


print(f'Продукт, принесший наибольшую выручку - {max_product[0]} на сумму {max_product[1]}')
print(f'Наибольшая сумма продаж была {max_day_sales[0]} на сумму {max_day_sales[1]}')

#### Построение графиков
fig, axs = plt.subplots(1, 2)

## 1. График общей суммы продаж по каждому продукту.
axs[0].set_title('Общие суммы продаж по каждому продукту')
axs[0].bar(total_sales_products.keys(), total_sales_products.values())

## 2. График общей суммы продаж по дням.
# получаем отсортированный по датам список
sorted_total_sales_over_time = sorted(total_sales_over_time.items())
x_axe = [x[0] for x in sorted_total_sales_over_time]    # данные для оси X
y_axe = [y[1] for y in sorted_total_sales_over_time]    # данные для оси Y
axs[1].set_title('Общие суммы продаж по дням')
axs[1].plot(x_axe, y_axe, marker='o')

# Отображение графиков
plt.show()