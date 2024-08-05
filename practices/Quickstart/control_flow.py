print("Control Flow")

a = False
if a:
    print("a is True")
else:
    print("a is False")
    
a =True
b= True
c=True

if a:
    print("a is True")
    if b:
        print("b is True")
        if c:
            print("c is True")
        else:
            print("c is False")
else : print("a is False")

# for loop
a = [3,4,6,7]

for item in a:
    print(item)

print(4 in a)

# while

a = 0;

while a < 5:
    print(a)
    a =a + 1

print("End of the program")