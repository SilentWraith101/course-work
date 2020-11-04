def shortBubbleSort(alist):

    exchanges = True
    passnum = len(alist)-1

    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                print(alist)
        passnum = passnum-1

alist = []
#alist=[20,18,27,9,11,2]
#alist = ['python','fortran','lisp','pascal','cobol','basic','jave']
shortBubbleSort(alist)
print(alist)

file_requested = input('Enter the file you want to use: ')

file_demo = open(file_requested, 'r')
contents = file_demo.read()
#File_opened = file_demo.read().strip(',').split(',')
file_demo.close()
print(contents)