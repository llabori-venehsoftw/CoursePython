#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:36:05 2020

@author: llabori
"""
""" Problema de la vida real extraido del Blog http://pythonpracticeprojects.com                      """
""" Contamos con una lista que posee recetas cada receta cuenta con sus ingredientes                  """
""" Cada receta tiene un tiempo de cocion + otras caracteritsicas ademas que las recetas por supuesto """
""" cuentan con parametros que pueden diferir unos de otros. Las recetas como tal son diccionarios    """ 

recipes = {
    'apple_pie': {
        'ingredients': ['flour', 'sugar', 'eggs', 'shortening', 'apples', 'cinnamon'],
        'cook_time': 60,
        'prep_time': 30,
        'ratings': {'john': 10, 'emily': 8, 'mom': 4}
    },
    'peanut_butter_cookies': {
        'ingredients': ['flour', 'sugar', 'peanut_butter', 'butter', 'eggs'],
        'cook_time': 45,
        'prep_time': 20,
        'allergens': ['peanuts']
    },
    'clam_chowder': {
        'ingredients': ['flour', 'milk', 'clams', 'vegetable_stock', 'salt'],
        'cook_time': 120,
        'prep_time': 30,
        'allergens': ['shellfish']
    }
}

""" Buscamos conocer si existe alguna calificacion para la receta por parte de jhon """
""" Una forma directa seria                                                         """
Result = False
if 'apple_pie' in recipes:
    if 'ratings' in recipes['apple_pie']:
        if 'john' in recipes['apple_pie']['ratings']:
            Result = True
print(Result)

""" Es factible utilizar todos los if concatenados utilizando una sola linea de instruccion """
if 'apple_pie' in recipes and 'ratings' in recipes['apple_pie'] and 'jhon' in recipes['apple_pie']['ratings']:
    Result = True

""" Con recursividad """
# El objetivo principal es obtener algo como:
# result = False
# if 'apple_pie/ratings/john' in flattened(recipes):
#   Result = True
# print Result
#
# print(type(recipes))
# print(isinstance(recipes, type(dict)))

def flattened_one(obj):
    if isinstance(obj, type(dict)):
        # If obj es un diccionario, flatten it one level.
        result = {}
        for key, value in obj.items():
            if isinstance(value, type(dict)):
                for subkey, subvalue in value.items():
                    flat_key = '/'.join([key, subkey])
                    result[flat_key] = subvalue
            else:
                result[key] = value
    else:
        # othersite just return the object
        return obj 
    
    return result      
print(flattened_one(recipes))

# La solucion anterior solo funciona en una parte del codigo por que no toma en
# cuenta los diccionarios anudados
#
def flattened_two(obj):
    if isinstance(obj, type(list)):
        # Is object is a list flatten every sub element
        result = []
        for elemt in obj:
            flat_elemt = flattened_two(elemt)
            result.append(flat_elemt)
    elif isinstance(obj, type(dict)):
        # If object is a dictionary, flatten in one level.
        result = {}
        for key, value in obj.items():
            if isinstance(value, type(dict)):
                flat_value = flattened_two(value)
                for subkey, subvalue in flat_value.items():
                    flat_key = '/'.join([key, subkey])
                    result[flat_key] = subvalue
            else:
                result[key] = value
    else:
        # othersite just return the object
        return obj 
    
    return result

print("\n\n=== Flattened ===\n\n")
print(flattened_two(recipes))

result2 = False
if 'apple_pie/ratings/john' in flattened_two(recipes):
    result2 = True
print(result2)