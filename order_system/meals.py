import venv
from menu import Menu
from collections import Counter
from custom_exceptions import TooManyItemsException

class Breakfast(Menu):
    def __init__(self):
        self.food_type = {
            "1" : "Eggs",
            "2" : "Toast",
            "3" : "Coffee"
        }
    
    def aggregate(self, food_tuple):
        return self.food_type[food_tuple[0]] if food_tuple[1]<2 else f"{self.food_type[food_tuple[0]]}({food_tuple[1]})"
    
    def get_food(self, order_list):
        print("Validating Breakfast Order..")
        self.validate(order_list)
        counter_list = Counter(order_list)
        print(counter_list)
        food_amount_list = [(item, amount) for item, amount in counter_list.items()]

        main = ""
        side = ""
        drink = ""
        print(food_amount_list)

        for k, v in food_amount_list:
            if k == "1":
                main = self.aggregate((k,v))
            elif k == "2":
                side = self.aggregate((k,v))
            elif k == "3":
                drink = self.aggregate((k,v))
            elif k == "Water":
                drink = k
        
        order = f"{main}, {side}, {drink}"
        print(order)
        return order

    
    def validate(self, order_list):
        if order_list.count("1") > 1 and order_list.count("2") > 1:
            raise TooManyItemsException(f"{self.food_type['1']} and {self.food_type['2']}")
        elif order_list.count("1") > 1:
            raise TooManyItemsException(f"{self.food_type['1']}")
        elif order_list.count("2") > 1:
            raise TooManyItemsException(f"{self.food_type['2']}")


class Lunch(Menu):
    def __init__(self):
        self.food_type = {
            "1" : "Sandwich",
            "2" : "Chips",
            "3" : "Soda"
        }
    
    def get_food(self, order_list):
        print("Validating Lunch Order...")
    
    def validate(self, order_list):
        pass

class Dinner(Menu):
    def __init__(self):
        self.food_type = {
            "1" : "Steak",
            "2" : "Potatoes",
            "3" : "Wine",
            "4" : "Cake"
        }
    
    def get_food(self, order_list):
        pass

    def validate(self, order_list):
        pass