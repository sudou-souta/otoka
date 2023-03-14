import sys

def loader():
    try:
        filename = sys.argv[1]
        f = open(filename,"r")
        src = f.read()
        f.close()
    except:
        print("Yu: open file error")
        sys.exit(0)
    tokens = src.split()
    tokens.append("pendp")
    return tokens


