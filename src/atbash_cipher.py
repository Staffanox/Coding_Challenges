# https://edabit.com/challenge/MGALfBAXhXqqdFyqo


def atbash(txt):
    table = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
             'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
             'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
             'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
             'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}
    encrypted_word = ""

    for letter in txt:
        if letter.isalpha():
            if letter.islower():
                encrypted_word += table.get(letter.upper()).lower()
            else:
                encrypted_word += table.get(letter)
        else:
            encrypted_word += letter
    return encrypted_word
