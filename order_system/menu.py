import abc, os, json
from collections import Counter

class Menu:
    def __init__(self, meal):
        self.meal = meal
        self.food_type = json.loads(os.getenv(meal))
        self.standard_item = json.loads(os.getenv(meal+"_STANDARD"))

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
            elif k == "Water" and self.meal.lower() != "dinner":
                drink += k
        
        if self.meal == "DINNER":
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