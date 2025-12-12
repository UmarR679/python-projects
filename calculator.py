import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

cal = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    print(art.logo)
    cont = True
    n1 = float(input("What's the first number?: "))
    while cont:
        for symbol in cal:
            print(symbol)
        operation_symbol = input("pick an operation: ")
        n2 = float(input("What's the second number?: "))
        ans = cal[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {ans}")

        choice = input(f"type 'y' to continue calculating with {ans} and 'n' to start new: ")

        if choice == "y":
            ans = n1
        else:
            cont == False
            print("\n" * 20)
            calculator()
calculator()



