def is_numeric(input_string) :
    """
    Returns True for valid numbers. Acceptable types of items: str or None
    """
    if input_string is None:
        return False

    try:
        input_string = input_string.strip()
        float(input_string)
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    # ---------------------------- TEST ---------------------------
    DIVIDER_DASH = '-' * 50
    GREEN_APPLE = '\U0001F34F'
    RED_APPLE = '\U0001F34E'

    test_input_strings = [None, "0  ", "0.1", "abc", "1 a", "2e10", "-90e3",
                          "1e", "e3", "6e-1", "99e2.5", "53.5e93", "--6", "-+3", "95a54e53"]

    count = 0
    for string in test_input_strings:
        print(DIVIDER_DASH)
        count += 1

        if is_numeric(string):
            print("{GREEN_APPLE} Test {count}: {string} is a valid number.".format(GREEN_APPLE=GREEN_APPLE, count=count, string=string))
        else:
            print("{RED_APPLE} Test {count}: `{string}` is not a valid number.".format(RED_APPLE=RED_APPLE, count=count, string=string))