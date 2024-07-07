import os

def get_user_input():
    """
    Prompts user for a word to encrypt and the cipher to use.

        Returns:
            tuple(word_in, cipher): if valid input is provided, 
                  otherwise (None, None).
                word_in(str): word entered by the user to be encrypted. 
                cipher(int): value of the cipher to apply to letters
                             of the word.
    """

    MIN_CIPHER_VALUE = 1
    MAX_CIPHER_VALUE = 25

    word_in = input('get_user_input(): Enter a word to encrypt, must be all lower-case letters: ')
    if word_in.isalpha() and word_in.islower():
        
        try: 
            cipher = int(input('get_user_input(): Enter a cipher, must be a number from 1 to 25: '))
            if MIN_CIPHER_VALUE <= cipher <= MAX_CIPHER_VALUE:
                return word_in, cipher
        except ValueError:
            print("get_user_input(): Invalid entry. Input for cipher must be a number between 1 and 25.")
        return None, None


def encrypt(word_to_encrypt, cipher):
    """
    Encrypts a word using a caesar cipher where each letter is shifted
    down the ascii code table for lower-case alphabet chars by the number 
    of the cipher. For example, if the cipher is 1, then the word 'abc' 
    becomes 'bcd'). If adding the cipher causes the new ascii code to 
    be shifted beyond 'z', the process wraps around to the beginning
    of the alphabet. For example, if the cipher is 1, then the word
    'xyz' becomes 'yza'.

        Args:
            word_to_encrypt(str): word to iterate and apply the 
                                  cipher to each letter. Assumed to be all 
                                  lower-case letters. 
            cipher(int): number to shift each letter down the alphabet.
                        Assumed to be between 1 and 25.

        Returns
            str: word resulting from the encryption process.
    """

    LOWER_LIMIT_ASCII_CODE = 96  # lower-case 'a' (97 offset by 1 to incl. 'a')
    UPPER_LIMIT_ASCII_CODE = 122  # lower-case 'z'
    new_char = ''
    encrypted_word = ''

    # Apply cipher to each letter of word
    for letter in word_to_encrypt:
        ascii_code = ord(letter)
        new_ascii_code = ascii_code + cipher

        # Wrap to begining of lower-case letters' ascii codes, if needed.
        if new_ascii_code > UPPER_LIMIT_ASCII_CODE:
            over_z_code = new_ascii_code - UPPER_LIMIT_ASCII_CODE
            new_ascii_code = LOWER_LIMIT_ASCII_CODE + over_z_code

        # Get the new letter.
        new_char = chr(new_ascii_code) 
        encrypted_word = encrypted_word + new_char
        #print(f'encrypt(): ecrypted_word: {encrypted_word}')

    print(f'encrypt(): returning ecrypted_word: {encrypted_word}')
    return encrypted_word


def main():
    os.system('cls')
    print(f'main(): Welcome!')
    cipher = 0
    encrypted_word = ''

    # Get user input & validate
    word_to_encrypt, cipher = get_user_input()
    if word_to_encrypt is None:
        return
    else:
        # Encrypt user's word with user's cipher
        encrypted_word = encrypt(word_to_encrypt, cipher)
        print(f'main(): using cipher: {cipher}, encrypted_word is: {encrypted_word}')

if __name__ == '__main__':  
    main()

