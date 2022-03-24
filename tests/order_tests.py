import sys
sys.path.append("../")
from order_system.order_system import OrderSystem
from order_system.custom_exceptions import OrderIncompleteException, TooManyItemsException
import pytest

order = OrderSystem()
def test_failed_order():
    with pytest.raises(OrderIncompleteException) as e_info:
        order.get_order("Breakfast", "3")
    message = e_info.value.args[0] if e_info.value.args else None
    assert message == "Unable to process: Main and Side is missing"

def test_breakfast():
    assert order.get_order("Breakfast", "1,2,3") == "Eggs, Toast, Coffee"
    assert order.get_order("Breakfast", "1,2,3,3,") == "Eggs, Toast, Coffee(2)"

def test_breakfast_toomany_excep():
    with pytest.raises(TooManyItemsException) as e_info:
        order.get_order("Breakfast", "1,1,2, 3")
    message = e_info.value.args[0] if e_info.value.args else None
    assert message == "Unable to process: Eggs cannot be ordered more than once" 

