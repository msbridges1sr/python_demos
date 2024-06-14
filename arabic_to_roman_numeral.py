SYMBOLS = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
}


def convert_to_roman(number):
    """Converts an Arabic number to its Roman numeral representation.

    Args:
        number: An integer between 1 and 3999 (inclusive).

    Returns:
        The Roman numeral representation of the number.

    Raises:
        ValueError: If the number is outside the supported range (1-3999).
    """

    if not 1 <= number <= 3999:
        raise ValueError("Number must be between 1 and 3999")

    roman_numeral = ""
    for value, symbol in sorted(SYMBOLS.items(), reverse=True):
        while number >= value:
            roman_numeral += symbol
            number -= value

    return roman_numeral


if __name__ == "__main__":
    while True:
        try:
            arabic_number = input("Enter an Arabic number between 1 and 3999 (or 'q' to quit): ")
            if arabic_number == 'q':
                break
            roman_numeral = convert_to_roman(int(arabic_number))
            print(f"The Roman numeral for {arabic_number} is: {roman_numeral}")
        except ValueError as e:
            print(f"Error: {e}")


