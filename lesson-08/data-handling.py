with open('datafile.dat','r') as fin:
    for line in fin:
        list = line.split(',')
        print(list)
        for item in list:
            print(item)
        number = int(list[1]) + int(list[2]) + int(list[3])
        print(f'The number for {list[0]} is {number}')
