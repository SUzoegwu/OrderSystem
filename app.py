from ordersystem.order_system import OrderSystem

from dotenv import load_dotenv
from flask import Flask, request, Response
import logging, os

# export FLASK_APP=routes.py
LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
# logging.basicConfig(filename="order_system.log", format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=LOG_LEVEL)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=LOG_LEVEL)    

print("Importing Environment Variables")
load_dotenv()

print("Creating application")
app = Flask(__name__)
ordersystem = OrderSystem()

def main():
    print("Starting application")
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get("HOST", "127.0.0.1")
    logging.info(f"Starting application on Host {host} and Port {port}")
    app.run(debug=True, host=host, port=port)

@app.route('/')
def my_order():
    try:
        logging.info("Application ready")
        meal = request.args.get('meal', type = str)
        order = request.args.get('order', type = str)
        logging.info(f"Received Request \n Meal: {meal}, Order {order}")
    
        returned_order = ordersystem.get_order(meal, order)
        return returned_order
    except Exception as e:
        return Response(e.message, status=e.status_code, mimetype='application/json')

if __name__ == '__main__':
    main()