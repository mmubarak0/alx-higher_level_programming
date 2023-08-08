#!/usr/bin/python3
def fizzbuzz():
    s = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            s.append("FizzBuzz")
        elif i % 3 == 0:
            s.append("Fizz")
        elif i % 5 == 0:
            s.append("Buzz")
        else:
            s.append(str(i))
    print(*s, sep=" ", end=" ")
