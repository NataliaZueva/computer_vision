with open('words.txt', 'r') as file:
    longest_word = ''
    for line in file:
        words = line.split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
print(f'longest word: {longest_word}')