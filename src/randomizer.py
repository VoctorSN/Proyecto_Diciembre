import random

def randomizer(l):
    if isinstance(l,list):
        random.shuffle(l)
        return l
    else:
        return "No list detected"

if __name__ == "__main__":
    from find_xspf import find_xspf
    from lector_dir import lector_dir
    print(randomizer(lector_dir(find_xspf())))
    # Para que el codigo funcione este print tiene que dar una lista desordenada de estos elementos