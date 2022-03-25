from order_system.menu import Menu
from order_system.custom_exceptions import TooManyItemsException, OrderIncompleteException

class Breakfast(Menu):
    def __init__(self, meal):
        super(Breakfast, self).__init__(meal)
    
    def get_food(self, order_list):
        print("Validating Breakfast Order...")
        self.validate(order_list)
        return self.aggregate(order_list)

    
    def validate(self, order_list):
        if order_list.count("1") > 1 and order_list.count("2") > 1:
            raise TooManyItemsException(f"{self.food_type['1']} and {self.food_type['2']}")
        elif order_list.count("1") > 1:
            raise TooManyItemsException(f"{self.food_type['1']}")
        elif order_list.count("2") > 1:
            raise TooManyItemsException(f"{self.food_type['2']}")


class Lunch(Menu):
    def __init__(self, meal):
        super(Lunch, self).__init__(meal)

    def get_food(self, order_list):
        print("Validating Lunch Order...")
        self.validate(order_list)
        return self.aggregate(order_list)
    
    def validate(self, order_list):
        if order_list.count("1") > 1 and order_list.count("3") > 1:
            raise TooManyItemsException(f"{self.food_type['1']} and {self.food_type['3']}")
        elif order_list.count("1") > 1:
            raise TooManyItemsException(f"{self.food_type['1']}")
        elif order_list.count("3") > 1:
            raise TooManyItemsException(f"{self.food_type['3']}")
        return

class Dinner(Menu):
    def __init__(self, meal):
        super(Dinner, self).__init__(meal)

    def get_food(self, order_list):
        print("Validating Dinner Order...")
        self.validate(order_list)
        return self.aggregate(order_list)

    def validate(self, order_list):
        if "4" not in order_list:
            raise OrderIncompleteException("Dessert")
        too_many_message = None
        single_order_list = ["1", "2", "3"]
        for i in single_order_list:
            if order_list.count(i) > 1:
                if too_many_message is None:
                    too_many_message = f"{self.food_type[i]}"
                else:
                    too_many_message += f" and {self.food_type[i]}"
        if too_many_message is not None:
            raise TooManyItemsException(too_many_message)
        return