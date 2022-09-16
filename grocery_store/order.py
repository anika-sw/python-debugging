


def create_order(products, customer_name):
    return {
        "customer_name": customer_name,
        "products": products,
    }

def add_product(order, product):
    order["products"].append(product)

def calculate_total(order):
    total = 0
    for i in range(0, len(order["products"])):
        total += order["products"][i]["price"]

    return total

    # product_one = create_product("Trombone", 478.95) 
    # product_two = create_product("Guitar", 327.99) 
    # product_three = create_product("Triangle", 2) {
    # products = [product_one, product_two, product_three]
    # products = [
    #   {"name": "trombone", "price": 478.95}, 
    #   {"name": "guitar", "price": 327.99}, 
    #   {"name": "triangle", "price": 2}
    # ]
    # order = create_order(products, "Shona Frederick")
    # create_order = {
    #   "customer name": "Shona Frederick", 
    #   "products":
    #       [
    #   {"name": "trombone", "price": 478.95}, 
    #   {"name": "guitar", "price": 327.99}, 
    #   {"name": "triangle", "price": 2}
    # ] }


    # # Act
    # total = calculate_total(order)