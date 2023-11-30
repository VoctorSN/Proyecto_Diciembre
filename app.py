from src.randomizer import randomizer
from src.lector_dir import lector_dir

def app():
    return randomizer(lector_dir())

print(app())