import random
import sys

def randomizer(unrandom_urls):
    if isinstance(unrandom_urls,list):
        random.shuffle(unrandom_urls)
        return unrandom_urls
    print("No list detected")
    sys.exit()

if __name__ == "__main__":
    from find_xspf import find_xspf
    from lector_dir import lector_dir
    print(randomizer(lector_dir(find_xspf())))
    # Para que el codigo funcione este print tiene que dar una lista desordenada de estos elementos
    randomizer("djadjawjda")
    # Para que funcione el if esa llamada deveria devolver unm print con el texto capturado