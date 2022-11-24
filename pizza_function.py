from utilts import  digame

def amount_extra(amount_slice):
    price = amount_slice * 2
    return price
def pizza_pices(size):
    pizza_size = ['S', 'M', 'L', 'XL']
    pizza_Pice = [40, 50, 60, 75]
    price = pizza_Pice[pizza_size.index(size)]
    return price
# to run function from utlits we need to call
digame()