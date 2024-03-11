import random

def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]


def write_data_to_file(filename, data):
    with open(filename, 'w') as file:
        for row in data:
            file.write(','.join(map(str, row)) + '\n')

def prepare_data(number_of_datarows):
    test_sets = []
    for i in range(1, number_of_datarows):
        test_sets.append(generate_random_data(random.randint(1000, 10000)))
    write_data_to_file(
        "../test_data.txt",
        test_sets)

prepare_data(1000)
