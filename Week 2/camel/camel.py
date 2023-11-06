camelCase = input("camelCase: ")

print("snake_case: ", end="")

for c in camelCase:
    if c.islower():
        print(c, end="")
    if c.isupper():
        print("_", c.lower(), end="", sep="")
print()
