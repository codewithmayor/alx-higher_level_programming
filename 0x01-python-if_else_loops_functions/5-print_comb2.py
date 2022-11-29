#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("0{}".format(i), end=", ")
    elif i > 9 and i < 100:
        print("{}".format(i), end=", ")
print("")        
