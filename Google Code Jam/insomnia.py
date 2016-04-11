__author__ = 'User'


N = 100


def find_number(N):
    used_digits = set()
    if N == 0:
        return "INSOMNIA"
    if N < 0:
        N = -N
    i = 0
    while len(used_digits) < 10:
        i += 1
        new_number = N*i
        digits = str(N*i)
        for digit in digits:
            used_digits.add(digit)
    return new_number

print(find_number(N))

with open("file_name.txt", "r") as file:
    with open("result.txt", "w") as write_file:
        for i, line in enumerate(file):
            x = find_number(int(line.strip()))
            write_file.write("Case #" + str(i+1) + ": " + str(x) + "\n")
