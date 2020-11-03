def writefile(value):
    with open('testdata.txt','a') as fout:
        fout.write(f'{value},')


def readline():
    with open('testdata.txt','r') as fin:
        data = fin.readline()
    return data


# section to input data
for i in range(5):
    data = int(input('Enter value: '))
    writefile(data)

# section to process data
data = readline()
list = data.split(',')
print(list)
list.pop(-1)
total = 0
for item in list:
    total += int(item)
print(f'Total is {total}')
