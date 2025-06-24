"""We no longer use Morse code to transfer information, but that doesn’t mean
you can’t use it in a code challenge. Write a function in Python that takes in a string
that can have alphanumeric characters in lower or upper case.
The string can also contain any special characters handled in Morse code, including commas,
colons, apostrophes, periods, exclamation marks, and question marks.
The function should return the Morse code equivalent for the string."""

def text_to_morse(s):
    morse_code_dict = {
        'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        '.': '.-.-.-', ',': '--..--', ':': '---...',
        '?': '..--..', "'": '.----.', '!': '-.-.--',
        ' ': '/'
    }

    s = s.upper()
    morse_words = []

    for word in s.split(' '):
        morse_letters = []
        for char in word:
            if char in morse_code_dict:
                morse_letters.append(morse_code_dict[char])
        morse_words.append(' '.join(morse_letters))
    
    return '  '.join(morse_words)
