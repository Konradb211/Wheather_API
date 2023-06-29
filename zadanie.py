import math

numDict = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

def decimal_to_any(num, system):
    numInSystem = ""

    while num > 0:
        if num % system < 10:
            numInSystem = str(num % system) + numInSystem
        else:
            numInSystem = numDict[num % system] + numInSystem
        num = math.floor(num / system)
    return  numInSystem


def binary_to_oct_or_hex(num, system):