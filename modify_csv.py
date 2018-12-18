import sys
if(len(sys.argv) != 2):
    print('input a file name in the command line')
else:    
    with open(sys.argv[1], "rt") as fin:
        with open(sys.argv[1]+"replaced.csv", "wt") as fout:
            for line in fin:
                fout.write(line.replace(' ', ','))