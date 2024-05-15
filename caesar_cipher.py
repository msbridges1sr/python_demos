# Helper Functions:

# Get the value from the dictionary with common notation
def get_value_from_key_common(dictionary, key):
    return dictionary[key]

# Get the value from the dictionary with .get() method
def get_value_from_key_method(dictionary, key):
    return dictionary.get(key)

# Get the key from the dictionary with .items() method
def get_key_from_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

# Get the key-value pair from the dictionary with .items() method
def get_key_value(dictionary, value):
      for key, val in dictionary.items():
        if val == value:
            return(key, value)
      return None

# Core Function: Encrypt the word
def encrypt(word, cipher):
  """ 
  This function encrypts a word using a Caesar Cipher, where each letter is 
  shifted a certain number of places down the alphabet (e.g., if cipher is 3, "hello" 
  becomes "khoor"). If the cipher causes the letter to shift beyond 'z' the shift 
  wraps to the beginning of the alphabet (e.g., if letter is 'y' and cipher is 2, 
  the encrypted letter is 'a'.)

    Args:
          word: the word to be encrypted. Assumed to be only lower-case letters.

          cipher: the number to shift down the alphabet.

    Returns
          encrypted_word: the word resulting from each letter being replaced with 
          the letter shifted down the alphabet by the number of positions defined 
          by the cipher
  """

  # Initialize the letters dictionary 
  letters_dict = {
      1:'a',
      2:'b',
      3:'c',
      4:'d',
      5:'e',
      6:'f',
      7:'g',
      8:'h',
      9:'i',
      10:'j',
      11:'k',
      12:'l',
      13:'m',
      14:'n',
      15:'o',
      16:'p',
      17:'q',
      18:'r',
      19:'s',
      20:'t',
      21:'u',
      22:'v',
      23:'w',
      24:'x',
      25:'y',
      26:'z'
  }

  print(f'now encrypting: {word}')
  encrypted_word = ''
  for val in word:
        key = get_key_from_value(letters_dict, val)
        new_key = key + cipher
        if new_key > 26:
            new_key = new_key - 26  # wrap around to the beginning of letters_dict.
        new_val = get_value_from_key_common(letters_dict, new_key)
        encrypted_word = encrypted_word + new_val
  return(encrypted_word)

# Define cipher value, max setting to use 25.
cipher = 25

# Prompt user for word to encrypt.
word = input('Enter a word to encrypt made up of only lower-case letters with no spaces: ')

# Validate word is only lower-case letters.
if word.isalpha() and word.islower() and word.count(' ') == 0:
    encrypted_word = encrypt(word, cipher)
    print(f'encrypted word = {encrypted_word}')
    print(f'psst ... cipher was: {cipher} ')
else:
    print('Invalid entry, word to encrypt must contain only lower-case letters with no spaces.')
