from src.randomizer import randomizer
from src.lector_dir import lector_dir

def app():
    return randomizer(lector_dir())
if __name__ == "__main__":
    print(app())