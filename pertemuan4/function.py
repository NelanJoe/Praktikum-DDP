# Function
def helloWorld():
    print("Hello World")

# Function with parameter
def sayHello(name):
    print(f"Hello {name}")

# Function with return value
def sum(a, b):
    return a + b

# Function with default parameter
def perkalian(a, b=2):
    return a * b


# Main function
def main():
    helloWorld()
    sayHello("John")
    print(sum(1, 2))
    print(perkalian(2))

if __name__ == "__main__":
    main()