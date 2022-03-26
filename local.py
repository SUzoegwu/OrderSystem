from order_system.order_system import OrderSystem
from order_system.custom_exceptions import OrderIncompleteException, UnknownItemException, TooManyItemsException
import sys

order_system = OrderSystem()

while True:
    meal = input("Please enter meal: ")
    order = input("Please enter order: ")
    try:
        print(order_system.get_order(meal, order))
    except TooManyItemsException as e:
        print("Error Code: " + str(e.status_code) + "\n" + e.message)
    except OrderIncompleteException as e:
        print("Error Code: " + str(e.status_code) + "\n" + e.message)
    except UnknownItemException as e:
        print("Error Code: " + str(e.status_code) + "\n" + e.message)