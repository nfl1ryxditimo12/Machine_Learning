def module_upper(price):#
    increment = price * 0.3
    upper_price = price + increment

    return upper_price

def module_lower(price):
    decrement = price * 0.3
    lower_price = price - decrement

    return lower_price

author = "pystock"

if __name__ == "__main__":
    print(module_lower(10000))
    print(module_upper(10000))
    print(__name__)