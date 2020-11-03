print('Reading with for loop')
filedemo = open('demotext.txt','r')
for line in filedemo:
    output = line
    print(f'Output line: {output}', end='')
filedemo.close()
