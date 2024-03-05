#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>

int median_low(std::vector<int> array) {
    std::vector<int> sorted_array = array;
    std::sort(sorted_array.begin(), sorted_array.end());
    int median_low;
    if (sorted_array.size() % 2 == 0) {
        median_low = sorted_array[sorted_array.size() / 2 - 1];
    } else {
        median_low = sorted_array[sorted_array.size() / 2];
    }
    return median_low;
}

void write_result_to_file(std::string filename, std::vector<int> data) {
    std::ofstream file(filename);
    if (file.is_open()) {
        for (int i = 0; i < data.size(); i++) {
            file << data[i];
            if (i != data.size() - 1) {
                file << ",";
            }
        }
        file << "\n";
        file.close();
    } else {
        std::cout << "Unable to open file";
    }
}

std::vector<std::vector<int>> read_data_from_file(std::string file_path) {
    std::vector<std::vector<int>> data;
    std::ifstream file(file_path);

//    std::ifstream file(file_path);
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            std::vector<int> row;
            size_t pos = 0;
            std::string token;
            while ((pos = line.find(',')) != std::string::npos) {
                token = line.substr(0, pos);
                row.push_back(std::stoi(token));
                line.erase(0, pos + 1);
            }
            row.push_back(std::stoi(line));
            data.push_back(row);
        }
        file.close();
    } else {
        std::cout << "Unable to open file1";
    }
    return data;
}

void test_correctness() {
    std::vector<std::vector<int>> loaded_data = read_data_from_file("C:\\Users\\march3wa\\Desktop\\Jezyki Skryptowe\\Lab_1\\test_data.txt");
    std::vector<int> results;
    for (std::vector<int> test_set : loaded_data) {
        int result = median_low(test_set);
        results.push_back(result);
    }
    write_result_to_file("C:\\Users\\march3wa\\Desktop\\Jezyki Skryptowe\\Lab_1\\cpp_result_data.txt", results);
}

void test_performance(int iterations) {
    std::vector<std::vector<int>> loaded_data = read_data_from_file("C:\\Users\\march3wa\\Desktop\\Jezyki Skryptowe\\Lab_1\\test_data.txt");

    auto start_time = std::chrono::high_resolution_clock::now();
    for (int i = 1; i < iterations; i++) {
        for (std::vector<int> test_set : loaded_data) {
            // Do nothing
        }
    }
    auto end_time = std::chrono::high_resolution_clock::now();
    double empty_time = std::chrono::duration_cast<std::chrono::duration<double>>(end_time - start_time).count();
    std::cout << "Empty Time: " << empty_time << " seconds" << std::endl;

    start_time = std::chrono::high_resolution_clock::now();
    for (int i = 1; i < iterations; i++) {
        for (std::vector<int> test_set : loaded_data) {
            median_low(test_set);
        }
    }
    end_time = std::chrono::high_resolution_clock::now();
    double execution_time = std::chrono::duration_cast<std::chrono::duration<double>>(end_time - start_time).count() - empty_time;
    std::cout << "Execution Time: " << execution_time << " seconds" << std::endl;
}

int main() {
    test_correctness();
//    test_performance(10000);
    return 0;
}

