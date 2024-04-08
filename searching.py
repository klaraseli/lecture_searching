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
    slovnik = {"pocet vyskytu" : vyskyty, "pozice vyskytu" : pozice}
    return slovnik


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    cislo = 5
    slovnik = linear_search(sequential_data, cislo)
    print(slovnik)


if __name__ == '__main__':
    main()