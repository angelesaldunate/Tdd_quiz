


def add_function(numbers, delimiter):
    if delimiter!= "":
        list_numbers = list(map(int, numbers.split(delimiter)))
    else:
        list_numbers = list(map(int, numbers.split(',')))
    return sum(list_numbers)