__author__ = 'User'


def fractiles(K, C, S):
    if C == 1:
        if S >= K:
            return [str(x+1) for x in range(K)]
        return ["IMPOSSIBLE"]
    if S < K // (C - 1):
        return ["IMPOSSIBLE"]
    if K == 1:
        return [str(K)]
    check_list = []
    i = 1
    while i < K:
        to_check = i
        iter_length = min(C - 1, K - i)
        for _ in range(iter_length):
            i += 1
            to_check = (to_check - 1) * K + i
        check_list.append(str(to_check))
    return check_list

with open("file_name.txt", "r") as file:
    with open("result.txt", "w") as write_file:
        for i, line in enumerate(file):
            if i == 0:
                continue
            input_list = line.strip().split(' ')
            x = fractiles(*[int(a) for a in input_list])
            write_file.write("Case #" + str(i) + ": " + " ".join(x) + "\n")
