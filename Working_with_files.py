from pprint import pprint


with open('recipes.txt', encoding='utf-8') as file:
    cook_book = dict()
    for dishes in file:
        dish = dishes.strip()
        variety_of_ingredients = int(file.readline())
        recipe = []
        for ingredient in range(variety_of_ingredients):
            ingredient_name, quantity, measure = file.readline().split('|')
            recipe.append({'ingredient_name': ingredient_name.strip(),
                           'quantity': int(quantity.strip()),
                           'measure': measure.strip()})
            cook_book[dish] = recipe
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    recipe = dict()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in recipe:
                    recipe[ingredient['ingredient_name']] = {
                        'quantity': ingredient['quantity'] * person_count,
                        'measure': ingredient['measure']
                    }
                else:
                    recipe[ingredient['ingredient_name']]['quantity'] += \
                        ingredient['quantity'] * person_count
        else:
            return f"Haven't recipe for {dish}"
    return recipe


# pprint(get_shop_list_by_dishes('Enter your list of dishes here', 'Enter the number of persons here'))
# print(get_shop_list_by_dishes('Enter your list of dishes here', 'Enter the number of persons here'))
