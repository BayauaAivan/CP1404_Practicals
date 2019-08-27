MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARACTERS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    print("Please enter a valid password: ")
    print("Password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARACTERS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Password is invalid")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password):
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    lower_count = 0
    upper_count = 0
    digit_count = 0
    special_count = 0
    for char in password:
        if char.isdigit():
            digit_count += 1
        elif char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        elif char in SPECIAL_CHARACTERS:
            special_count += 1

    if lower_count == 0 or upper_count == 0 or digit_count == 0:
        return False

    if SPECIAL_CHARACTERS_REQUIRED:
        if special_count == 0:
            return False
    return True


main()
