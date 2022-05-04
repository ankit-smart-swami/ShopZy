from django import template

register = template.Library()

@register.filter(name="currency")
def currency(price):
    return "₹ " + str(price)

@register.filter(name="total_val")
def total_val(qty, price):
    return qty * price

@register.filter(name="colour")
def colour(status):
    if status == 'Pending':
        return 'danger'
    elif status == 'Order Placed':
        return 'warning'
    elif status == 'Shipped':
        return 'secondary'
    elif status == 'On the Way':
        return 'info'
    elif status == 'Delivered Soon':
        return 'primary'
    elif status == 'Delivered':
        return 'success'
    