"""
Pizza Ordering System

"""


class Pizza:
    def __init__(self, description, cost):
        self.__description = description
        self.__cost = cost
    
    def get_description(self):
        return self.__description
    
    def get_cost(self):
        return self.__cost

# Klasik, Margherita, Türk Pizzası, Dominos Pizza vb. pizza sınıflarını oluşturun.
class ClassicPizza(Pizza):
    def __init__(self):
        self.description = "Classic Pizza"
        self.cost = 8.99

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description
        
class NeapolitanPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Neapolitan Pizza"
        self.cost = 10.99
        
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turk Pizza"
        self.cost = 19.99
        
class ChicagoPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Chicago Pizza"
        self.cost = 12.99

class GreekPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Greek Pizza"
        self.cost = 9.99
        

class CaliforniaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "California Pizza"
        self.cost = 15.99

# Bir Decorator sınıfı oluşturun ve belirlediğiniz sosların her birini bir sınıf olarak tanımlayın.
class SauceDecorator(Pizza):
    def __init__(self, component):
        self.component = component
        self.cost = 0.0
        
    def get_cost(self):
        return self.component.get_cost() + self.cost
        
    def get_description(self):
        return self.component.get_description()

class YogurtSauce(SauceDecorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 2.99
        self.description_addition = "Yogurt Sauce"
        
    def get_description(self):
        return self.component.get_description() + ", " + self.description_addition

class GarlicBread(SauceDecorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 5.99
        self.description_addition = "Garlic Bread"
        
    def get_description(self):
        return self.component.get_description() + ", " + self.description_addition

class MexicanSauce(SauceDecorator):
    def __init__(self, component):
        super().__init__(component)
        self.cost = 2.99
        self.description_addition = "Mexican Sauce"
        
    def get_description(self):
        return self.component.get_description() + ", " + self.description_addition
        


