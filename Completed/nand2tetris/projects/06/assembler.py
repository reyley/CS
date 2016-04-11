# Rachel Ilan. April 8th 2016
__author__ = "Rachel"

import re
from itertools import combinations


variable_converter = {
    "SCREEN": 16384,
    "KBD": 24576,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4
}
jump_conversion = {
    "JMP": "111",
    "JEQ": "010",
    "JGT": "001",
    "JLT": "100",
    "JNE": "101",
    "JGE": "011",
    "JLE": "110"
}
dest_conversion = {}
calculation_converter = {
    "0": "101010",
    "1": "111111",
    "-1": "111010",
    "D": "001100",
    "A": "110000",
    "!D": "001101",
    "!A": "110001",
    "-D": "001111",
    "-A": "110011",
    "D+1": "011111",
    "A+1": "110111",
    "D-1": "001110",
    "A-1": "110010",
    "D+A": "000010",
    "D-A": "010011",
    "A-D": "000111",
    "D&A": "000000",
    "D|A": "010101"
}

# not_allowed_chars =
new_variable_location = 16
comment_symbol = "//"
address_symbol = "@"
dest_symbol = "="
jump_symbol = ";"
file_removed_ws = []
translated_file_lines = []


def insert_calculation(calculation):
    if "A" in calculation:
        m_calculation = calculation.replace("A", "M")
        calculation_converter[m_calculation] = "1" + calculation_converter[calculation]
    calculation_converter[calculation] = "0" + calculation_converter[calculation]


def add_default_variables():
    global calculation_converter
    for i in range(16):
        variable_converter["R" + str(i)] = i
    for dest in substrings("AMD"):
        dest_conversion[dest] = destination_code(dest)
    keys = list(calculation_converter.keys())
    for calculation in keys:
        insert_calculation(calculation)


def substrings(parent_string):
    _substrings = []
    for i in range(1, len(parent_string)+1):
        _substrings.extend(["".join(substring) for substring in combinations(parent_string, i)])
    return _substrings


def destination_code(dest):
    code = ["0", "0", "0"]
    if "A" in dest:
        code[0] = "1"
    if "M" in dest:
        code[2] = "1"
    if "D" in dest:
        code[1] = "1"
    return "".join(code)


def translate_file(file_name):
    with open(file_name, "r") as read_file:
        for line in read_file:
            line = remove_whitespace(line)
            line = insert_variables(line)
            if line:
                file_removed_ws.append(line)
    with open(file_name + ".hack", "w") as write_file:
        for line in file_removed_ws:
            line = translate_line(line) + "\n"
            write_file.write(line)


def insert_variables(line):
    if line and line[0] == "(":
        variable = line[1:]
        location = len(file_removed_ws)
        variable_converter[variable] = location
        return ""

    return line


def remove_whitespace(line):
    if line:
        line = line.split(comment_symbol)[0]
        line = re.sub(r"[^A-Za-z0-9@;=\-_(+!&|.$:]", "", line)
    return line


def translate_line(line):
    if line[0] == "@":
        return a_line(line)
    return d_line(line)


def is_int(_str):
    try:
        int(_str)
        return True
    except ValueError:
        return False


def a_line(line):
    global new_variable_location
    address = line[1:]
    if is_int(address):
        int(address)
    else:
        if address not in variable_converter:
            variable_converter[line[1:]] = new_variable_location
            new_variable_location += 1
        address = variable_converter[address]
    binary_address = "{0:b}".format(int(address))
    if len(binary_address) > 15:
        raise IndexError("Address out of bounds")
    return "0"*(16-len(binary_address)) + binary_address


def d_line(line):
    code = "111"
    dest_code = "000"
    calculation_code = "0"*7
    jump_code = "000"

    if dest_symbol in line:
        split_line = line.split(dest_symbol)
        dest = split_line[0]
        dest_code = dest_conversion[dest]
        line = split_line[1]

    if jump_symbol in line:
        split_line = line.split(jump_symbol)
        line = line.split(jump_symbol)[0]
        jump_code = jump_conversion[split_line[1]]

    if line:
        calculation_code = calculation_converter[line]

    return code + calculation_code + dest_code + jump_code

add_default_variables()
translate_file("rect/Rect.asm")