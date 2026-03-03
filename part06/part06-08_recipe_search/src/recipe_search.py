# Write your solution here
def read_file(filename):
  recipes_dict = {}
  with open(filename) as recipes:
    recipe_name = True
    ingredients = []

    for line in recipes:
      line = line.strip()

      if recipe_name:
        name = line
        recipes_dict[name] = {}
        recipe_name = False
        continue

      if line == "":
        recipes_dict[name]["ingredients"] = ingredients
        recipe_name = True
        ingredients = []
        continue

      if line.isdecimal():
        time = int(line)
        recipes_dict[name]["time"] = time
        continue

      ingredients.append(line)

    recipes_dict[name]["ingredients"] = ingredients
  return recipes_dict

def search_by_name(filename: str, word: str) -> list:
  found_recipes = []
  recipes = read_file(filename)
  for recipe_name in recipes:
    if word.lower() in recipe_name.lower():
      found_recipes.append(recipe_name)
  return found_recipes

def search_by_time(filename: str, prep_time: int) -> list:
  found_recipes = []
  recipes = read_file(filename)
  for recipe_name, values in recipes.items():
    if values["time"] <= prep_time:
      found_recipes.append(f"{recipe_name}, preparation time {values['time']} min")
  return found_recipes

def search_by_ingredient(filename: str, ingredient: str) -> list:
  found_recipes = []
  recipes = read_file(filename)
  for recipe_name, values in recipes.items():
    if ingredient.lower() in values["ingredients"]:
      found_recipes.append(f"{recipe_name}, preparation time {values['time']} min")
  return found_recipes

if __name__ == "__main__":
  # found_recipes = search_by_name("recipes1.txt", "cake")
  # found_recipes = search_by_time("recipes1.txt", 20)
  found_recipes = search_by_ingredient("recipes1.txt", "eggs")
  for recipe in found_recipes:
      print(recipe)
