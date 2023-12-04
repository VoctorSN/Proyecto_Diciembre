import os

def find_xspf(location=""):
    if location=="":
        return [file for file in os.listdir() if file.endswith(".xspf")]
    return [file for file in os.listdir(location) if file.endswith(".xspf")]

if __name__ == "__main__":
    print(find_xspf("C:/Users/a23victorsn/Desktop"))
    