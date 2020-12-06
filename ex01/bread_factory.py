from bread import Bread

class BreadFactory:
  def create_bread(self, bread_type, recipe):
    return Bread(bread_type, recipe)