from constants import *
import glob
import errno
import json

def main():
    path = ENCOUNTER_DIR + "/*.json"
    files = glob.glob(path)
    idx = 0
    files_dict = {}
    for name in files:
        fidx = name.rfind("/")
        if fidx == -1:
            display = name
        else:
            display = name[fidx + 1:-5]
        print("(" + str(idx) + ")", display)
        files_dict[idx] = display
        idx += 1
    return files_dict

def display():
    data = main()
    inp = input("select encounter to describe")
    split = data[int(inp)].split("\\") #data[int(inp)] is encounter\"name", when only "name" is needed. Therefore, the string is split
    with open(split[1], "r") as f:
        print(json.dumps(json.load(f), indent=4))

if __name__ == '__main__':
    print(main())
