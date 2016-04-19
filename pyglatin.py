pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) < 0 and original.isalpha():
    print '%s try again' % original
else:
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = word[1:] + first + pyg
    print '%s'% new_word
