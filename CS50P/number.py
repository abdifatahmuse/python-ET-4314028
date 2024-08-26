try:
    c = int(input("What is x?"))
    print(f"the x is {c}")
    
except ValueError:
    print("Invalid input, is not integer")