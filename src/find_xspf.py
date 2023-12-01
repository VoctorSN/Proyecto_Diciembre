import os 
def find_xspf():
    return [file for file in os.listdir() if file.endswith(".xspf")]

if __name__ == "__main__":
    print(find_xspf())