import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as file:
        content = json.load(file)
        klice = content.keys()
        for data in klice:
            if data == field:
                value = content[field]
                return value
        return None

def linear_search(sekvence, hledane_cislo):
    vyskyty = 0
    pozice = []
    for idx, cislo in enumerate(sekvence):
        if cislo == hledane_cislo:
            vyskyty = vyskyty + 1
            pozice.append(idx)
    slovnik = {"pocet vyskytu": vyskyty, "pozice vyskytu": pozice}
    return slovnik

def pattern_search(sekvence, vzor):
    delka = len(vzor)
    if delka % 2 == 0:
        stred = delka / 2
    if delka % 2 == 1:
        stred = int(delka / 2) + 1
    delka_sekvence = len(sekvence)
    pozice = []
    for idx in range(delka_sekvence):
        zkoumame = sekvence[idx:delka + idx]
        if zkoumame[0] != vzor[0]:
            continue
        if zkoumame == vzor:
            pozice.append(idx + stred - 1)
    return pozice

def binary_search(seznam, hledane_cislo):
    neco = False
    soubor = seznam
    while neco == False:
        delka = len(soubor)
        if delka % 2 == 0:
            stred = delka / 2
        elif delka % 2 == 1:
            stred = int(delka / 2) + 1
        if hledane_cislo == stred:
            neco == True
        elif hledane_cislo > stred:
            soubor = soubor[stred:]
        elif hledane_cislo < stred:
            soubor = soubor[:stred]


def main():
    sequential_data = read_data("sequential.json", "ordered_numbers")
    print(sequential_data)
    # cislo = "A"
    # slovnik = linear_search(sequential_data, cislo)
    # print(slovnik)
    # vzor = "ATA"
    # sekvence = pattern_search(sequential_data, vzor)
    # print(sekvence)


if __name__ == '__main__':
    main()