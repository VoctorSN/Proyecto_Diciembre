import random

def randomizer(l):
    assert isinstance(l,list)
    random.shuffle(l)
    return l


if __name__ == "__main__":
    print(randomizer([1,23,52,4,23,123,1]))