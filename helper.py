# -*- coding: utf-8 -*-
virama = "\u0C4D"
dependent_vowel_signs = ('\u0C3E', '\u0C3F', '\u0C40', '\u0C41', '\u0C42', '\u0C43', '\u0C44',
                         '\u0C45', '\u0C46', '\u0C47', '\u0C48', '\u0C49', '\u0C4A', '\u0C4B',
                         '\u0C4C', '\u0C00', '\u0C01', '\u0C02', '\u0C03')
vowel_cosonant_signs = ('\u0C05', '\u0C06', '\u0C07', '\u0C08', '\u0C09', '\u0C0A', '\u0C0B',
                        '\u0C0C', '\u0C0D', '\u0C0E', '\u0C0F', '\u0C10', '\u0C11', '\u0C12',
                        '\u0C13', '\u0C14', '\u0C15', '\u0C16', '\u0C17', '\u0C18', '\u0C19',
                        '\u0C1A', '\u0C1B', '\u0C1C', '\u0C1D', '\u0C1E', '\u0C1F', '\u0C20',
                        '\u0C21', '\u0C22', '\u0C23', '\u0C24', '\u0C25', '\u0C26', '\u0C27',
                        '\u0C28', '\u0C29', '\u0C2A', '\u0C2B', '\u0C2C', '\u0C2D', '\u0C2E',
                        '\u0C2F', '\u0C30', '\u0C31', '\u0C32', '\u0C33', '\u0C34', '\u0C35',
                        '\u0C36', '\u0C37', '\u0C38', '\u0C39')
zwnj = "\u200C" # zero width non-joiner

# def int_to_char(i):
#     '''used for returning hex-unicode values from decimal'''
#     return "\\u0{}".format(hex(i)[2:].upper())
# temp = [str(int_to_char(c)) for c in range(3077, 3130)]

def get_chars(word):
    '''Returns the characters constituting the inputted Telugu word.'''
    length = len(word)
    stack = list()
    i = 0
    while i < length:
        if word[i] == virama and i+1 < length:
            try:
                prev = stack.pop()
            except IndexError:
                return None
            if word[i+1] != zwnj: # if next character isn't a zero width non-joiner
                stack.append(prev+word[i]+word[i+1])
            else:
                stack.append(prev+word[i])
                stack.append(word[i+1])
            i+=2
            continue
        elif word[i] == virama and i+1 == length:
            try:
                prev = stack.pop()
            except IndexError:
                return None
            stack.append(prev+word[i])
            i+=1
            continue
        elif word[i] in dependent_vowel_signs:
            try:
                prev = stack.pop()
            except IndexError:
                return None
            stack.append(prev+word[i])
        elif word[i] in vowel_cosonant_signs:
            stack.append(word[i])
        else:
            # unrecognized character
            pass
        i+=1
    return stack

s = "శ్రీధామ"

for c in s:
    print(c)
print(get_chars(s))
