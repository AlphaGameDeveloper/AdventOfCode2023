import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: %s <INPUT-FILE>" % sys.argv[0])
        return
    filep = sys.argv[1]
    if os.path.isfile(filep) == False:
        print("error: Cannot find file '%s'" % filep)
        return 1
    file = open(filep, "r")
    lines = [line.replace("\n", "") for line in file.readlines()]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    sum = 0
    for line in lines:
        foundnumbers = []
        # get all numbers
        for char in line:
            if char in numbers:
                foundnumbers.append(int(char))

        n1 = foundnumbers[0]
        n2 = foundnumbers[len(foundnumbers) - 1]
        n = int(str(n1) + str(n2))
        sum += n
    print("Total sum: {}".format(sum))

if __name__ == "__main__":
    main()