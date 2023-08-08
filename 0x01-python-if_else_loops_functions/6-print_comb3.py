#!/usr/bin/python3
print(", ".join(
         [", ".join(["{}{}".format(i, j) for j in range(i+1, 10)]) for i in range(9)]))
