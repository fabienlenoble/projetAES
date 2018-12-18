import sys
if(len(sys.argv) == 1):
    print('input a file name in the command line')
else:
    fp = open(sys.argv[1], "r")
    print(fp.readline())
    print(fp.readline())
    print(fp.readline())