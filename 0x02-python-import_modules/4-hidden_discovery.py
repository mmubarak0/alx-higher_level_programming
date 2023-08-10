#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hid
    for name in dir(hid):
        if name[0:2] != '__':
            print(name)
