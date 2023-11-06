str = input("Input: ")

vowels = ["a", "e", "i", "o", "u"]
for c in str:
    if c.lower() in vowels:
        continue
    else:
        print(c, end="")
print()
