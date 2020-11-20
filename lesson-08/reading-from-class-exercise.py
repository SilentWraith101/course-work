def readline():
    with open('class_exercise.txt','r') as fin:
        data = fin.readline()
    return data


data = readline()
list = data.split(',')
print(list)
list.pop(-1)
total = 0

for item in list:
    total += int(item)
print(f'Total is {total}')

print('The average value is: ', sum(data)/len(data))


