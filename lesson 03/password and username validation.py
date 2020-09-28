username = str(input('Enter a username: '))
password = str(input('Enter a password: '))

while True:
    validateUsername = str(input('Enter a username: '))
    validatePassword = str(input('Enter a password: '))
    if validateUsername != username and validatePassword != password:
        print('lock')
    else:
        print('unlock')
        break
