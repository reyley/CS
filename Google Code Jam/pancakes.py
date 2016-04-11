__author__ = 'User'

pancakes = ""


def flip_pancakes(pancakes):
    flips = 0
    for last_pancake, pancake in zip(pancakes[:-1], pancakes[1:]):
        if not pancake == last_pancake:
            flips += 1
    if pancakes and pancakes[-1] == "-":
        flips += 1
    return flips


with open("file_name.txt", "r") as file:
    with open("result.txt", "w") as write_file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            x = flip_pancakes(line.strip())
            write_file.write("Case #" + str(i) + ": " + str(x) + "\n")