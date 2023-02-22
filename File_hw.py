from pprint import pprint

def menu_sort(file):
    with open(file, encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.strip()
            ingredients_count = int(f.readline())
            ingredients = []
            for c_l in range(ingredients_count):
                aei = f.readline().strip()
                ingredient_name, quantity, measure = aei.split(' | ')
                ingredients.append(
                    {'ingredient_name' : ingredient_name,
                     'quantity' : quantity,
                     'measure' : measure}
                )

            cook_book[dish_name] = ingredients
            f.readline()
        pprint(cook_book, sort_dicts=False, width=100)

menu_sort('recipes.txt')

