import random

def randomizer(l):
    if isinstance(l,list):
        random.shuffle(l)
        return l
    else:
        return "No list detected"

if __name__ == "__main__":
    print(randomizer([1,23,52,4,23,123,1]))
    # Para que el codigo funcione este print tiene que dar una lista desordenada de estos elementos