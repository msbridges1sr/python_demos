# This program validates that a user-specified username satisfies the validation criteria 
# provided. Specifically, the following four criteria:
#
# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character. 
#
# The username is passed to the function validate_username() performs tests on the username.
# If a criteria fails to be met, it raises a ValueError with a informative user message. 
# Upon successful validation, the function returns 'True' and prints a message indicating 
# that the username is valid, otherwise returns 'False'.   

def validate_username(username):
    try:
        # Test whether username length is between 4 and 25 chars long, inclusive
        l = len(username)
        if not (4 <= l <= 25):
            raise ValueError('Invalid, length must be between 4 and 25 characters.')
        
        # Test whether username starts with a letter
        first_char = username[0]
        if not first_char.isalpha():
            raise ValueError('Invalid, first character must be a letter.')
            
        # Test whether username ends with an underscore
        last_char = username[l-1]
        if not last_char != '_':
            raise ValueError('Invalid, last character must not be an underscore.')

        # Test whether username contains only letters or underscores
        for char in username:
                if not (char.isalnum() or char == '_'):
                    raise ValueError('Invalid, must only use alphabetic, numeric, or underscore characters.')
                
        return True

    except ValueError as e:
        print(f'Error: {e}')
        return False

# Print user instructions
print(f"""
Please make a username that meets the following criteria:
   It must be between 4 and 25 characters.
   It must start with a letter.
   It can only contain letters, numbers, and the underscore character.
   It cannot end with an underscore character. 
""")

# Prompt for username input
input_username = input('Enter username: ')

# Call validation function passing input username
rc = validate_username(input_username)
if rc:
    print(f'Username \'{input_username}\' is valid')
