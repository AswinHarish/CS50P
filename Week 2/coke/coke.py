due = 50
print(f"Amount Due: {due}")

while due != 0:
    coin = int(input("Insert Coin: "))

    if coin != 50 and coin != 25 and coin != 10 and coin != 5:
        print(f"Amount Due: {due}")
        continue
    else:
        due -= coin
        if due <= 0:
            print(f"Change Owed: {abs(due)}")
            break
        else:
            print(f"Amount Due: {due}")
