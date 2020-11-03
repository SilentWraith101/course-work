print('File opened and read from')

filedemo = open('demotext.txt','r')
for line in filedemo:
    print(line)
filedemo.close()
