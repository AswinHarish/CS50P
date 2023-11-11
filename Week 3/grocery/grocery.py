cart = {}

while True:
    try:
        item = input().upper()
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
    except EOFError:
        cart = dict(sorted(cart.items()))
        for i in cart:
            print(f"{cart[i]} {i}")
        break
