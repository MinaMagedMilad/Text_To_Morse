ttm_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

# Reverse the dictionary
mtt_dict = {value: key for key, value in ttm_dict.items()}
keep_translator_on = True
while keep_translator_on:
    direction = input("Enter 'ttm' (text to Morse) or 'mtt' (Morse to text): ").lower()
    word = input("Enter your word or Morse code: ").lower()
    output = ''

    if direction == 'ttm':
        for letter in word:
            if letter != ' ':
                output += ttm_dict[letter] + ' '
            else:
                output += '  '  # Double space between words
        print("Morse Code:", output.strip())

    elif direction == 'mtt':
        morse_letters = word.split(' ')
        for symbol in morse_letters:
            if symbol == '':
                output += ' '  # Detect double space for word separation
            else:
                output += mtt_dict[symbol]
        print("Text:", output)

    else:
        print("Invalid direction. Use 'ttm' or 'mtt'.")

    decision = input("Do you want to resume? Y/N: ").lower()
    if decision == 'n':
        keep_translator_on = False
        print("Thanks see you later ❤")