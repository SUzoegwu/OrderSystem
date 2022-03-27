## Order System
This project is an OrderSystem that takes an an order and returns the correct order.

## Installation with PyPI
pip install ordersystem

## Extras
Clone and follow the ReadMe in this [repository](https://github.com/SUzoegwu/OrderSystemServer) to see the Flask and Docker version of this application.

## Usage
Ensure these environment variables are set:

`MENU, COMPLIMENTARY, SINGLE_ITEM, MEAL_CATEGORY_MAPPING COURSE_CATEGORY_MAPPING, MANDATORY_COURSE`

Example as below:

```
MENU="{\"breakfast\":{\"1\":\"Eggs\",\"2\":\"Toast\",\"3\":\"Coffee\"},\"lunch\":{\"1\":\"Sandwich\",\"2\":\"Chips\",\"3\":\"Soda\"},\"dinner\":{\"1\":\"Steak\",\"2\":\"Potatoes\",\"3\":\"Wine\",\"4\":\"Cake\"}}"

COMPLIMENTARY="{\"breakfast\":{\"main\":\"\",\"side\":\"\",\"drink\":\"\"},\"lunch\":{\"main\":\"\",\"side\":\"\",\"drink\":\"\"},\"dinner\":{\"main\":\"\",\"side\":\"\",\"drink\":\"Water\",\"dessert\":\"\"}}"

SINGLE_ITEM="{\"breakfast\":[\"1\",\"2\"],\"lunch\":[\"1\",\"3\"],\"dinner\":[\"1\",\"2\",\"3\"]}"

COURSE_CATEGORY_MAPPING="{\"main\":\"1\",\"side\":\"2\",\"drink\":\"3\",\"dessert\":\"4\"}"

MANDATORY_COURSE="{\"breakfast\":[\"main\",\"side\"],\"lunch\":[\"main\",\"side\"],\"dinner\":[\"main\",\"side\",\"dessert\"]}"

```

MENU references the actual menu of your ordering system. It maps the COURSE_CATEGORY_MAPPING to the actual food. 
COMPLIMENTARY is food items that is always included in the order such as this restaurant always want water to be included in dinner orders.
SINGLE_ITEM are list of courses that could be ordered only once. In this restaurant, a Breakfast order cannot have more than 1 order of Eggs or Toast
COURSE_CATEGORY_MAPPING maps the courses to the number category used by the other environment variables. Orders will be returned in the same placement as it is set in the course category. In this restaurant, the order will be returned with the main as first, the side as second and the drink as third
MANDATORY_COURSE is a dictionary where the keys is the meal you want and the value is a list of the course that must be ordered with the meal. In this restaraunt, every meal must have a main and side course ordered.

To add the to the menu, first create a mapping in the COURSE_CATEGORY_MAPPING for the specific course. The set the number mapping to a food item in the Menu dictionary. Feel free to add to COMPLIMENTARY and SINGLE_ITEM if you need to make adjustments. For example, this restaurant now wants to add Crab Cakes as an appetizer to its list of options for dessert. The following environment variables will be set:

```
MENU="{\"breakfast\":{\"1\":\"Eggs\",\"2\":\"Toast\",\"3\":\"Coffee\"},\"lunch\":{\"1\":\"Sandwich\",\"2\":\"Chips\",\"3\":\"Soda\"},\"dinner\":{\"1\":\"Steak\",\"2\":\"Potatoes\",\"3\":\"Wine\",\"4\":\"Cake\", \"5\":\"CrabCakes\"}}"

COMPLIMENTARY="{\"breakfast\":{\"main\":\"\",\"side\":\"\",\"drink\":\"\"},\"lunch\":{\"main\":\"\",\"side\":\"\",\"drink\":\"\"},\"dinner\":{\"main\":\"\",\"side\":\"\",\"drink\":\"Water\",\"dessert\":\"\"}}"

SINGLE_ITEM="{\"breakfast\":[\"1\",\"2\"],\"lunch\":[\"1\",\"3\"],\"dinner\":[\"1\",\"2\",\"3\"]}"

COURSE_CATEGORY_MAPPING="{\"main\":\"1\",\"side\":\"2\",\"drink\":\"3\",\"dessert\":\"4\", \"appetizers\":\"5\"}"

MANDATORY_COURSE="{\"breakfast\":[\"main\",\"side\"],\"lunch\":[\"main\",\"side\"],\"dinner\":[\"main\",\"side\",\"dessert\"]}"
```


In your code, you can do the following.

```
from ordersystem.order_system import OrderSystem

ordersystem = OrderSystem()
ordersystem.get_order("Breakfast", "1,2,3")

```