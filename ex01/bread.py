class Bread:
  def __init__(self, bread_type, recipe):
    self.bread_type = bread_type
    self.recipe = recipe

  def get_info(self):
    print(f'breadType: {self.bread_type}')
    print('recipe')
    for ingredient, quantity in self.recipe.items():
      print(f'{ingredient}: {quantity}')
    print()