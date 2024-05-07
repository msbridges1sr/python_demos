import re


def clean_and_format(str):
    """
    Cleans and formats a phone number string consistently.

    This function removes non-numeric characters from the input string,
    ensures it contains exactly 10 digits, and formats it with parentheses
    around the area code and hyphens separating the three-digit segments.

    Args:
        str: The unformatted phone number string.

    Returns:
        The formatted phone number string, or -1 if the input is invalid.
    """

    # Clean the string of all but numbers
    clean_str = ''.join(num for num in str if num.isnumeric())
    if clean_str.isalnum() and len(clean_str) == 10:

        # Format the phone number using regular expressions
        pattern = r"(\d{3})(\d{3})(\d{4})"
        valid_str = re.sub(pattern, r"(\1) \2-\3", clean_str)
        return valid_str
    else:
        print(f'clean_and_format(): Failed, this cleaned str does not have precisely 10 numbers: {clean_str}')
        return(-1)
    
# Initialize ph_list of unformatted phone numbers
ph_list = ['(551) 123 4567', '662-234-5678', '773 8901234', '884---901---2345','995!@  9 08970%^&*  11']
print(f'ph_list before: {ph_list}')

# Update phone numbers in ph_list with valid formatting applied
for index, ph_num in enumerate(ph_list):
    valid_num = clean_and_format(ph_num)
    if valid_num == -1:
        print(f'main: warning, ph_list[{index}] not updated [\'{ph_list[index]}]')
    else:    
        ph_list[index] = valid_num

print(f'ph_list after: {ph_list}')