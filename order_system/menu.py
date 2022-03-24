import abc

class Menu:
    def __init__(self):
        pass

    @abc.abstractmethod
    def validate(self, order_list):
        return
    
    @abc.abstractmethod
    def get_food(self, order_list):
        return