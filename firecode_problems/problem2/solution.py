def dec_to_bin(number):
    if number == 1:
        return "1"
    elif number == 0:
        return "0"
    else:
        return dec_to_bin(number / 2) + dec_to_bin(number % 2)
