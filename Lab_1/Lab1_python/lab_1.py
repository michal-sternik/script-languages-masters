import statistics
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
    results_builtIn = []
    for test_set in loaded_data:
        result = median_low(test_set)
        results.append(result)
        result_builtIn = statistics.median_low(test_set)
        results_builtIn.append(result_builtIn)
    write_result_to_file("../python_result_data.txt", results)
    write_result_to_file("../python_result_builtIn_data.txt", results_builtIn)

def test_performance():
    loaded_data = read_data_from_file('../test_data.txt')
    # blad wzgledny -2 <= x-xprim <= 2
    # |x-xprim| <= 2s
    # dla bledu pomiaru 1s to bedzie 2s bo w jedna i druga strone wiec 2/x-2
    #dla x=200 bedzie 2/198 *100% czyli wiecej niz 1 wiec za malo
    #calculate time needed for empty loop
    start_time = time.time()
    for n in range(1, 700):
        for test_set in loaded_data:
            pass
    end_time = time.time()
    empty_time = end_time - start_time
    print(f"Empty Time: {empty_time:.6f} seconds")


    start_time = time.time()
    for n in range(1, 700):
        for test_set in loaded_data:
            median_low(test_set)
        print(n)
    end_time = time.time()
    print(end_time - start_time - empty_time)
    print("blad wzgledny: " +  str((4 / ( (end_time - start_time - empty_time) - 4 ) ) * 100)  + "%" )
    execution_time = end_time - start_time - empty_time
    print(f"Execution Time: {execution_time:.6f} seconds")

    start_time = time.time()
    for n in range(1, 700):
        for test_set in loaded_data:
            statistics.median_low(test_set)
    end_time = time.time()
    execution_time = end_time - start_time - empty_time
    print(f"Execution Time (build-in function): {execution_time:.6f} seconds")


# Testowanie poprawności
# test_correctness()
test_performance()

