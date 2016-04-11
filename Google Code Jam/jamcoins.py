__author__ = 'User'

import datetime


def has_small_divisors(number):
    if number <= 1 or number % 2 == 0:
        return 0
    check = 3
    maxneeded = number
    while check < maxneeded+1 and check < 100:
        maxneeded = number/check
        if number % check == 0:
            return check
        check += 2
    return False


def base_convert(binary_string, base):
    n = 0
    new_number = 1
    for i, char in enumerate(binary_string[::-1]):
        if char == "1":
            n += new_number
        new_number *= base
    return n


def check_jam(possible_jam):
    divisors = []
    for i in range(2, 11):
        convert = base_convert(possible_jam, i)
        divisor = has_small_divisors(convert)
        if divisor:
            divisors.append(str(divisor))
        else:
            return False, []
    return True, divisors


def random_jam_coin_generator(size, num_jams):
    start = datetime.datetime.now()
    if size < 2:
        return "1"*size
    jams = {}
    found = 0
    middle_decimal = 0
    while found < num_jams:
        binary_middle = "{0:b}".format(middle_decimal)
        if size - len(binary_middle) - 2 < 0:
            "TOO MAAAANNNNNNNNNNYyyyyyy"
            break
        binary_middle = "0"*(size - len(binary_middle) - 2) + binary_middle
        possible_jam = "1" + binary_middle + "1"
        is_jam, divisors = check_jam(possible_jam)
        if is_jam:
            found += 1
            jams[possible_jam] = divisors
        middle_decimal += 1
    print(datetime.datetime.now() - start)
    return jams

with open("result.txt", "w") as write_file:
    jams = random_jam_coin_generator(32, 50000)
    write_file.write("Case #1:\n")
    for i, jam in enumerate(jams):
        write_file.write(jam + " " + " ".join(jams[jam]) + "\n")
