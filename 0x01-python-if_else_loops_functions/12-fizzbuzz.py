#!/usr/bin/python3
def fizzbuzz():
    for i in range(101):
        if i % 3 == 0 or i % 5 == 0:
            if i % 3 == 0:
                print("Fizz", end="")
            if i % 5 == 0:
                print("Buzz", end="")
            print(" ", end="")
            break
    else:
        print(f"{i:d}", end=" ")
    print("")
