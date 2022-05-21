"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""



def main(sold_up):
    summ_of_all_item = 0
    number_of_sold = 0
    for any_item in sold_up:
      summ_for_item = 0
      for mean in range(len(any_item["items_sold"])):
        summ_for_item +=any_item["items_sold"][mean]
      average_summ_for_item = summ_for_item / len(any_item["items_sold"])
      print(f"Телефонов модели {any_item['product']}, всего продано: {summ_for_item}")
      print(f"Среднее колличество продаж {any_item['product']}:{round(average_summ_for_item)}")


      summ_of_all_item += summ_for_item
      number_of_sold += len(any_item["items_sold"])
      average_sum_for_all = summ_of_all_item // number_of_sold

      print(f"Всего продано, различных моделей телефонов:{summ_of_all_item}")
      print(f"Cреднее колличество проданных телефонов : {average_sum_for_all}")    

phone_base = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]  
if __name__ == "__main__":
    main(phone_base)
