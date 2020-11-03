fout = open('datafile.dat', 'w')
fout.write('data1,30,40,50\n')
fout.write('data2,45,67,87\n')
fout.write('data3,87,43,45\n')
fout.close()

with open('datafile.dat','r') as fin:
    for line in fin:
        print (line)
