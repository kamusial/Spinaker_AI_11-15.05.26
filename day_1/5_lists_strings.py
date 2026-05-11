text = 'doggy'

print(text)
print(text[0])  # 1st letter
print(text[3])  # 4st letter

my_list = ['doggy', 'cat', 'bird', 'cow', 'parrot']
print(my_list)   # display whole list
print(my_list[3])   # display 4th element
# print(my_list[5])  # 6th element

word = input('Give a word:  ')

# for i in range(len(word)):
#     if word[i] == 'a':
#         print(f'Yes, I found letter a in possition {i+1}')

counter_a = 0
for letter in word:
    # print(letter)
    if letter == 'a':
        print('Yes, I found letter a')
        counter_a = counter_a + 1
print(f'I found {counter_a} letters a')
