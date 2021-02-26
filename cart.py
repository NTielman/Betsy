from queries import get_product


class Cart(object):

    def __init__(self, session):
        '''checks if a cart already exists in session
        and initializes cart'''
        if 'cart' in session:
            cart = session['cart']
        else:
            cart = {}
        self.cart = cart

    def __iter__(self):
        '''makes Cart instance itterable'''
        for product_id in self.cart.keys():
            self.cart[str(product_id)]['product'] = get_product(product_id)
        for cart_item in self.cart.values():
            cart_item['total_price'] = cart_item['product']['price_in_cents'] * \
                cart_item['quantity']
            yield cart_item

    def __len__(self):
        '''defines the value returned when len() is called on cart instance'''
        return sum(cart_item['quantity'] for cart_item in self.cart.values())

    def add_product(self, product_id, quantity=1):
        '''adds a product to cart'''
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity, 'id': product_id}
        else:
            self.cart[product_id]['quantity'] += int(quantity)

            if self.cart[product_id]['quantity'] == 0:
                self.remove_product(product_id)
        return self.cart

    def remove_product(self, product_id):
        '''removes cart item(s)'''
        if product_id in self.cart:
            del self.cart[product_id]
            return self.cart

    def get_total_cost(self):
        '''returns the total cost for all items in the cart'''
        for product_id in self.cart.keys():
            self.cart[str(product_id)]['product'] = get_product(product_id)
        return sum(cart_item['quantity'] * cart_item['product']['price_in_cents'] for cart_item in self.cart.values())
