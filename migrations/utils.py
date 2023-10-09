def process_orders(orders, criterion):
    if criterion == 'completed':
        filtered_orders = [order for order in orders if order['status'] == 'completed']
    elif criterion == 'pending':
        filtered_orders = [order for order in orders if order['status'] == 'pending']
    elif criterion == 'canceled':
        filtered_orders = [order for order in orders if order['status'] == 'canceled']
    else:
        filtered_orders = orders

    total_income = sum(order['quantity'] * order['price'] for order in filtered_orders)
    return total_income
