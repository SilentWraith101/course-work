with open('datafile.dat', 'r') as fin:
    for line in fin:
        list = line.split(',')
        print(list)
