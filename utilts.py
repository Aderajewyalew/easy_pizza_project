import  random
def digame():
    dic_persent = 0
    chance1 = random.randint(1,9)
    chance2 = random.randint(1, 9)
    dic_persent += (chance1 * chance2) / 100
    return  dic_persent