import time


def median_low(array):
    sorted_array = sorted(array)
    median_low = sorted_array[len(sorted_array)//2 - 1] if len(sorted_array) % 2 == 0 else sorted_array[len(sorted_array)//2]
    return median_low


def write_result_to_file(filename, data):
    print(data)
    with open(filename, 'w') as file:
        file.write(','.join(map(str, data)) + '\n')

def read_data_from_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split(',')))
            data.append(row)
    return data
def test_correctness():
    loaded_data = read_data_from_file('../test_data.txt')
    results = []
    for test_set in loaded_data:
        result = median_low(test_set)
        results.append(result)
    write_result_to_file("../python_result_data.txt", results)

def test_performance(iterations):
    loaded_data = read_data_from_file('../test_data.txt')

    #calculate time needed for empty loop
    start_time = time.time()
    for _ in range(1, iterations):
        for test_set in loaded_data:
            pass
    end_time = time.time()
    empty_time = end_time - start_time
    print(f"Empty Time: {empty_time:.6f} seconds")


    start_time = time.time()
    for _ in range(1, iterations):
        for test_set in loaded_data:
            median_low(test_set)
    end_time = time.time()
    execution_time = end_time - start_time - empty_time
    print(f"Execution Time: {execution_time:.6f} seconds")


# Testowanie poprawności
test_correctness()
# test_performance(10000)

