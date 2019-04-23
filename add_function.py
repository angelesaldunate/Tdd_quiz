


def add_function(numbers, delimiter):
    if delimiter == "":
        delimiter = ","
    list_numbers = list(map(int, numbers.split(delimiter)))
    list_numbers = [item for item in list_numbers if item >= 0]
    return sum(list_numbers)