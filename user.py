class User:

    selected_ingredients = None

    def __init__(self):
        self.selected_ingredients = []

    def get_ingredients(self):
        return self.selected_ingredients

    def add_ingredient(self, ingredient):
        self.selected_ingredients.append(ingredient)
    
    def delete_ingredient(self, ingredient):
        self.selected_ingredients.remove(ingredient)
    
    def isSelected(self, ingredient):
        return self.selected_ingredients.count(ingredient) > 0