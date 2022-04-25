from django import template

register = template.Library()

@register.filter(name="is_in_cart")
def is_in_cart(product, cart):
    keys = cart.keys()
    #print(cart)
    
    for key in keys :
        if int(key) == product.id and cart[key] != 0 :
            return True
    return False

@register.filter(name="cart_quantity")
def cart_quantity(product, cart):
    keys = cart.keys()
    #print(cart)
    for key in keys :
        if int(key) == product.id :
            return cart[key]
        
@register.filter(name="total_price") 
def total_price(product, cart):
    qty = cart_quantity(product,cart)
    return product.price * qty

@register.filter(name="grand_total")
def grand_total(products, cart):
    g_total = 0
    for product in products:
        g_total += total_price(product,cart)
        
    return g_total


