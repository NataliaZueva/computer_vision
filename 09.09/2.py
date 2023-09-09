word = input('Enter a word in English: ')
vowels = 'aeiouyAEIOUY'
num_v, num_c = 0, 0
for letter in word:
    if letter in vowels:
        num_v += 1
    else:
        num_c += 1
print(f'Number of vowels/consonants: {num_v}, {num_c}')
