import random
words = ['java','python','javascript','swift','cobol']
chosen_words = random.choice(words)
word_display = ['_' for _ in chosen_words]
attempt = 8

print('welcome to H_a_n_g_m_a_n')

while attempt > 0 and '_' in word_display:
    print('\n' + ' '.join(word_display))
    guess = input('Guess a letter: ').lower()
    if guess in chosen_words:
        for index,letter in enumerate(chosen_words):
            if letter == guess:
                word_display[index] = guess
    else:
        print('That letter does not appear in the word')
        attempt -= 1

if '_' not in word_display:
    print('You guessed the word' )
    print(' '.join(word_display))
else:
    print('You lost , the word is '+chosen_words)


