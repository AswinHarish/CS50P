 # main function
def main():
    name = input("Whats you name: ")
    hello(name)


# function to print name
def hello(name):
    print(f"Hello, {name}")

# calling main
if __name__ == "__main__":
    main()
