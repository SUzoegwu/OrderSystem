## Order System
This project is an OrderSystem that takes an an order and returns the correct order.

## Installation with PyPI
pip install ordersystem

Installing project with pypi will not include flask REST API and Docker. To retrieve the Dockerfile and flask application. Clone this [repository](https://github.com/SUzoegwu/OrderSystem) and follow the rest of this Readme in the Git clone section.

## Usage
Ensure these environment variables are set:

`MENU, COMPLIMENTARY, SINGLE_ITEM, MEAL_CATEGORY_MAPPING`

Example as below:

```
MENU="{\"breakfast\":{\"1\":\"Eggs\",\"2\":\"Toast\",\"3\":\"Coffee\"},\"lunch\":{\"1\":\"Sandwich\",\"2\":\"Chips\",\"3\":\"Soda\"},\"dinner\":{\"1\":\"Steak\",\"2\":\"Potatoes\",\"3\":\"Wine\",\"4\":\"Cake\"}}"

COMPLIMENTARY="{\"breakfast\":{\"main\":\"\",\"side\":\"\",\"drink\":\"\"},\"lunch\":{\"main\":\"\",\"side\":\"\",\"drink\":\"\"},\"dinner\":{\"main\":\"\",\"side\":\"\",\"drink\":\"Water\",\"dessert\":\"\"}}"

SINGLE_ITEM="{\"breakfast\":[\"1\",\"2\"],\"lunch\":[\"1\",\"3\"],\"dinner\":[\"1\",\"2\",\"3\"]}"

MEAL_CATEGORY_MAPPING="{\"main\":\"1\",\"side\":\"2\",\"drink\":\"3\",\"dessert\":\"4\"}"

```

In your code, you can do the following.

```
from ordersystem.order_system import OrderSystem

ordersystem = OrderSystem()
ordersystem.get_order("Breakfast", "1,2,3")

```