from order_system.order_system import OrderSystem

from dotenv import load_dotenv
from flask import Flask, request, Response
import logging, os

# export FLASK_APP=routes.py    

print("Importing Environment Variables")
load_dotenv()

print("Creating application")
app = Flask(__name__)
ordersystem = OrderSystem()

def main():
    print("Starting application")
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='127.0. 0.1', port=port)
    app.run()

@app.route('/')
def my_order():
    try:
        print("Application ready")
        meal = request.args.get('meal', type = str)
        order = request.args.get('order', type = str)
    
        returned_order = ordersystem.get_order(meal, order)
        return returned_order
    except Exception as e:
        return Response(e.message, status=e.status_code, mimetype='application/json')

if __name__ == '__main__':
    main()