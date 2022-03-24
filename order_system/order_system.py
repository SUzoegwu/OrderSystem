from order_system.meals import Breakfast, Lunch, Dinner
import logging, os
from order_system.custom_exceptions import OrderIncompleteException

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=LOG_LEVEL)

class OrderSystem:
    def __init__(self):
        self.menu_mapping = {
            "breakfast" : Breakfast(),
            "lunch" : Lunch(),
            "dinner" : Dinner()
        }

    def get_order(self, menu_type, order):
        order = order.replace(" ", "")
        order_list = order.split(",")
        logging.debug(f"Received order: {menu_type} List of items: {order_list}")
        logging.info("Validating food")
        self.validate(order_list)
        logging.info("Done Validating")

        if "3" not in order_list:
            logging.info("Drink is not included. Adding water...")
            order_list.append("Water")
        
        logging.info("Getting the menu")
        menu = self.menu_mapping[menu_type.lower()]

        logging.info(f"Getting the food for {menu}")
        return menu.get_food(order_list)



    def validate(self, order_list):
        logging.info(f"Validating {order_list}")
        if "1" not in order_list and "2" not in order_list:
            raise OrderIncompleteException("Main and Side")
        elif "1" not in order_list:
            raise OrderIncompleteException("Main")
        elif "2" not in order_list:
            raise OrderIncompleteException("Side")
        
        logging.info("Done validating")
        return