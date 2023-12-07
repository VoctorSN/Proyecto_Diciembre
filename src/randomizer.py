import random

def randomizer(unrandom_urls):
    if not unrandom_urls:
        return None
    if isinstance(unrandom_urls,list):
        random.shuffle(unrandom_urls)
        return unrandom_urls

if __name__ == "__main__":
    from find_xspf import find_xspf
    from lector_dir import lector_dir
    print(randomizer(lector_dir(find_xspf())))
    # Para que el codigo funcione este print tiene que dar una lista desordenada de estos elementos