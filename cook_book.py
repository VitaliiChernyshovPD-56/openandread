import os
from pprint import pprint

path = os.getcwd()
file_name = 'recipes.txt'
full_path  = os.path.join(path, file_name)

def open_file(file_path, mode='rt'):
    with open(file_path, mode, encoding='utf-8') as file:
            cook_book = {}

            for line in file:
                dish_name = line.strip()
                ingredient = int(file.readline().strip())
                dish = []

                for item in range(ingredient):
                    ingredient_list = file.readline().strip().split(' | ')
                    d = {}
                    for i in range(len(ingredient_list)):
                        d['ingredient_name'] = ingredient_list[0]
                        d['quantity'] = ingredient_list[1]
                        d['measure'] = ingredient_list[2]
                    dish.append(d)
                file.readline()
                cook_book[dish_name] = dish
            pprint(cook_book)
open_file(full_path)


