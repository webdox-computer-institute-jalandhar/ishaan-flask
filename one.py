def shop(gift):
    def wrapper():
        return gift() + " is my gift"
    return wrapper



# @shop
def mygift():
    return "watch"


# print(mygift())


print(shop(mygift)())


