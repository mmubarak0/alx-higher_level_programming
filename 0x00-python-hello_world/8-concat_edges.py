#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[(47 - 8): (75 - 8)] + str[(73 + 42 - 8): (73 + 47 - 8)] + str[:6]
print(str)
