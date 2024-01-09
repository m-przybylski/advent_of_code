input = "day15"
max_teaspoons = 100
def parse_data(line: str):
    name, ingredients = line.split(": ")
    ingredients = [(prop, int(val)) for prop, val in [ingredient.split() for ingredient in ingredients.split(", ")]]
    recipe = {}
    for ingredient, value in ingredients:
        recipe[ingredient] = value
    return (name, recipe)

def get_score(teaspoons: dict, recipe: dict):
    capacity = durability = flavor = texture = calories = 0
    for teaspoon in teaspoons:
        capacity += teaspoons[teaspoon] * recipe[teaspoon]["capacity"]
        durability += teaspoons[teaspoon] * recipe[teaspoon]["durability"]
        flavor += teaspoons[teaspoon] * recipe[teaspoon]["flavor"]
        texture += teaspoons[teaspoon] * recipe[teaspoon]["texture"]
        calories += teaspoons[teaspoon] * recipe[teaspoon]["calories"]
    
    return (max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0), calories)

def get_best_score(
        ingredients: list[str], 
        teaspoons: dict, 
        total_teaspoons: int, 
        recipe: dict
    ):
    ingredients_copy = ingredients.copy()
    best_score = 0
    name = ingredients_copy.pop()
    for i in range(total_teaspoons + 1):
        teaspoons[name] = i
        if len(ingredients_copy) == 0:
            if sum(teaspoons.values()) != 100:
                continue
            # get_score({ "Butterscotch": 44 , "Cinnamon": 56}, recipe)
            # 62842880
            score, _ = get_score(teaspoons, recipe)
            best_score = max(best_score, score)
        else:
            best_score = max(best_score, get_best_score(ingredients_copy, teaspoons, total_teaspoons - i, recipe))


    return best_score

def get_best_score_with_max_calories(
        ingredients: list[str], 
        teaspoons: dict, 
        total_teaspoons: int, 
        recipe: dict,
        calories: int
    ):
    ingredients_copy = ingredients.copy()
    best_score = 0
    name = ingredients_copy.pop()
    for i in range(total_teaspoons + 1):
        teaspoons[name] = i
        if len(ingredients_copy) == 0:
            if sum(teaspoons.values()) != 100:
                continue
            # get_score({ "Butterscotch": 44 , "Cinnamon": 56}, recipe)
            # 57600000
            score, cookie_calories = get_score(teaspoons, recipe)
            if cookie_calories != calories:
                continue
            best_score = max(best_score, score)
        else:
            best_score = max(best_score, get_best_score_with_max_calories(ingredients_copy, teaspoons, total_teaspoons - i, recipe, calories))


    return best_score


recipe = {}
ingredients = list(map(parse_data, open(input).read().splitlines()))
for ingredient in ingredients:
    recipe[ingredient[0]] = ingredient[1]


print(get_best_score(list(recipe.keys()), {}, 100, recipe))
print(get_best_score_with_max_calories(list(recipe.keys()), {}, 100, recipe, 500))
