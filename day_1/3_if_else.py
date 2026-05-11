age = int(input('How old are you?   '))
print(f'You are {age} years old')
print(f'You were born in {2026-age} year')

if age < 18:
    print('You are not adult')
    print('ask you mom')
elif age == 18:
    print('you are young adult')
else:
    print('you are adult, make your decission')

print('program continues')

