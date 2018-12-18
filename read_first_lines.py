import sys
if(len(sys.argv) != 3 ):
    print('input a file name and a number of line in the command line')
else:
    fp = open(sys.argv[1], "r")
    for i in range(int(sys.argv[2])):
        print(fp.readline())