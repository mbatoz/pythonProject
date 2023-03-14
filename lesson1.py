user_name = input('Enter your name: ')
age = int(input('Enter your birth year: ')) # преобразование типов данных
current_age = 2023 - age
message = 'Hello, '
print('Your age is: ' + str(current_age))

print(f'{message}{user_name}. Your age is: {current_age}')

print('{} {}. Your age is: {}'.format(message, user_name, current_age))