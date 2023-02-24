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
        return cook_book

pprint(menu_sort('recipes.txt'), sort_dicts=False, width=100)


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = menu_sort('recipes.txt')
    ingredients_count = {}
    for dish in dishes:
        if dish in cook_book:
            for all_ingredients in cook_book[dish]:
                if all_ingredients['ingredient_name'] not in ingredients_count:
                    ingredients_count[all_ingredients['ingredient_name']] = {'measure':all_ingredients['measure'], 'quantity': int(all_ingredients['quantity']) * person_count}
                else:
                    ingredients_count[all_ingredients['ingredient_name']]['quantity'] += int(all_ingredients['quantity']) * person_count
    pprint(ingredients_count)

get_shop_list_by_dishes(['Омлет','Фахитос'], 2)
