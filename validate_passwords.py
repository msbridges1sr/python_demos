
def validate_password(password_str):
    """
    Validates the strength of a password based on complexity rules. 
    
        Args:
            password_str (str): The password to validate.
            
        Returns: 
            str: A message indicating the password's validity or specific
                 reasons for invalidity.

    """
    
    MIN_LENGTH = 8
    char_counts = {"upper": 0, "lower": 0, "digit": 0}
    min_chars = {"upper": 1, "lower": 1, "digit": 1}

    # Check password length
    if len(password_str) < MIN_LENGTH:
        return('pw invalid, must be a least 8 characters long.')

    # Check for alphanumeric characters only
    if not password_str.isalnum():
        return('pw invalid, must contain letters and numbers only.')
    
    # Count character types
    for char in password_str:
        if char.isalpha():
            char_counts["upper"] += char.isupper()
            char_counts["lower"] += char.islower()
        elif char.isnumeric():
            char_counts["digit"] += 1

    # Check character type counts
    for char_type, min_count in min_chars.items():
         if char_counts[char_type] < min_count:
              return(f'Password invalid, must contain at least {min_count} {char_type}s')
    
    # Password is valid
    return("Password is valid.")
           
# Print validation requirements. 
prompt = """
Password requirements:
* Must be at least 8 characters long
* Must contain at least one upper-case letter
* Must contain at least one lower-case letter
* Must contain at least one number
"""
print(prompt)

# Prompt user for password to validate.
password_str = input('Enter a password to validate: ')
result = validate_password(password_str)
print(result)
