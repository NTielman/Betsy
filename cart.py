from queries import get_product

class Cart(object):

    def __init__(self, session):
        '''checks if a cart already exists in session
        and initializes cart'''
        # self.session = session
        # cart = self.session.get('cart')
        if 'cart' in session:
            cart = session['cart']
        # cart = session.get('cart')
        else:
            cart = {}
        
        # check session if cart exists else, create an empty dict and pass it to session as cart
        # if not cart:
        #     # cart = self.session['cart'] = {}
        #     cart = {}
        self.cart = cart

    def __iter__(self):
        for product_id in self.cart.keys():
            self.cart[str(product_id)]['product'] = get_product(product_id)
        for cart_item in self.cart.values():
            cart_item['total_price'] = cart_item['product']['price_in_cents'] * cart_item['quantity']
            yield cart_item

    def __len__(self):
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

        # self.save_cart()
        return self.cart

    def remove_product(self, product_id):
        '''removes cart item(s)'''
        if product_id in self.cart:
            del self.cart[product_id]
            # self.save_cart()
            return self.cart

    # def save_cart(self):
    #     '''saves the cart to session'''
    #     # self.session['cart'] = self.cart
    #     session['cart'] = self.cart
    #     # self.session.modified = True
    #     session.modified = True

    def get_total_cost(self):
        '''returns the total cost for all items in the cart'''
        for product_id in self.cart.keys():
            self.cart[str(product_id)]['product'] = get_product(product_id)
        return sum(cart_item['quantity'] * cart_item['product']['price_in_cents'] for cart_item in self.cart.values())

'''{
                prod_id1:{
                    product: Product(obj)
                    quantity: 5
                    total_price: 250 (korda /100 pa get price in dollars ipv cents)
                }
                prod_id2:{
                    product: Product(obj)
                    quantity: 2
                }
                prod_id3:{
                    product: Product(obj)
                    quantity: 8
                }
            }'''