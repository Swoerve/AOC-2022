with open('1/1.txt') as f:
    lines = f.readlines()
    poop = ""
    poop = [ poop + line for line in lines]
    print(poop)