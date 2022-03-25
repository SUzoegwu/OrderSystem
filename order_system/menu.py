import abc, os, json
from collections import Counter

from order_system.custom_exceptions import UnknownItemException

class Menu:
    def __init__(self, meal):
        print("Initializing Menu")
        self.meal = meal.lower()
        self.menu = json.loads(os.getenv("MENU"))
        self.food_type = self.menu[meal]
        self.complimentary_items = json.loads(os.getenv("COMPLIMENTARY"))
        self.standard_item = self.complimentary_items[meal]

    def aggregate(self, order_list):
        # food_type = json.loads(os.getenv(meal))
        # standard_item = json.loads(os.getenv(meal+"_STANDARD"))
        # self.food_type = json.loads(food)
        def aggregator(food_tuple):
            return self.food_type[food_tuple[0]] if food_tuple[1]< 2 else f"{self.food_type[food_tuple[0]]}({food_tuple[1]})"
        print("Counting the list of items")
        counter_list = Counter(order_list)
        print(counter_list)
        food_amount_list = [(item, amount) for item, amount in counter_list.items()]

        main = self.standard_item.get("main", "")
        side = self.standard_item.get("side", "")
        drink = self.standard_item.get("drink", "")
        dessert = self.standard_item.get("dessert", None)
        for k, v in food_amount_list:
            if k == "1":
                main += aggregator((k,v)) if main == "" else main + ", " +  aggregator((k,v))
            elif k == "2":
                side += aggregator((k,v)) if side == "" else side + ", " +  aggregator((k,v))
            elif k == "3":
                drink = aggregator((k,v)) if drink == "" else drink + ", " +  aggregator((k,v))
            elif k == "4" and dessert is not None:
                dessert = aggregator((k,v)) if dessert == "" else dessert + ", " +  aggregator((k,v))
            elif k == "Water":
                if self.meal.lower() != "dinner":
                    drink += k
            else:
                raise UnknownItemException(str(k))
        
        if self.meal == "dinner":
            order = f"{main}, {side}, {drink}, {dessert}"
        else:
            order = f"{main}, {side}, {drink}"
        return order

    @abc.abstractmethod
    def validate(self, order_list):
        return
    
    @abc.abstractmethod
    def get_food(self, order_list):
        return