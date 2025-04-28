#for row in range(1,11):
    #for col in range(row):
    #print('*' , end=' ')
    #print()

for row in range(1,11):
    for col in range(row):
        print('*',end='')
    for space  in range(10-row):
        print(' ',end='')

    print(' ' ,end='')

    for col in range(11 - row):
        print('*',end='')
    for space in range(row - 1):
        print(' ',end='')

    print(' ',end='')

    for space in range(row -1):
        print(' ',end='')
    for col in range(11 - row):
        print('*',end='')

    print(' ',end='')

    for space in range(10 - row):
        print(' ',end='')
    for col in range(row):
        print('*',end='')

    print()
