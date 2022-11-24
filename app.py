from  pizza_function import amount_extra
from pizza_function import pizza_pices
from pizza_function import digame

# all code are in one function called app

def app():
    delivery_costB = 20
    delivery_costO = 60

    # these variable are outside loop cuase no needs ask for costomer reaptdly

    age = int(input("please enter the age: "))
    game = input("do you want play a game?\n if you play you will have discont y/n")
    destnation = input("enter your destnation: ")
    total = 0
    while age > 18:
        size = input("please enter  the pizza size: ")
        extra = input("do you want extar? ")

        if extra == "yes":
            amount_slice = int(input("enter amount of slice you  need: "))
            sum = amount_extra(amount_slice)
            total += sum
        if game != "no":
            digame()
            print(f"total discount is {digame()}")
        if destnation == "beersheba":
            sum = pizza_pices(size) + delivery_costB
            total += sum
        else:
            sum = pizza_pices(size) + delivery_costO
            total += sum
        con = input("do you want continue: ")
        if con == "no":
            break
    else:
        print("Sorry you can not get an access! good bay! ")
    print(f'The total pyament is {total} ')
    print(f'The total pyament with discount is {round(total * (1 - digame()))} ')
