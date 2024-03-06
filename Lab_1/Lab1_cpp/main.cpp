#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;

int median_low(vector<int> array) {
// we work on array copy so theres no need to do anything
    sort(array.begin(), array.end());
    int median_low;
    if (array.size() % 2 == 0) {
        median_low = array[array.size() / 2 - 1];
    } else {
        median_low = array[array.size() / 2];
    }
    return median_low;
}

void write_result_to_file(string filename, vector<int> data) {
    ofstream file(filename);
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
        cout << "Unable to open file";
    }
}

vector<vector<int>> read_data_from_file(string file_path) {
    vector<vector<int>> data;
    ifstream file(file_path);

//    ifstream file(file_path);
    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            vector<int> row;
            size_t pos = 0;
            string token;
            while ((pos = line.find(',')) != string::npos) {
                token = line.substr(0, pos);
                row.push_back(stoi(token));
                line.erase(0, pos + 1);
            }
            row.push_back(stoi(line));
            data.push_back(row);
        }
        file.close();
    } else {
        cout << "Unable to open file";
    }
    return data;
}

void test_correctness() {
    vector<vector<int>> loaded_data = read_data_from_file("../../test_data.txt");
    vector<int> results;
    for (vector<int> test_set : loaded_data) {
        int result = median_low(test_set);
        results.push_back(result);
    }
    write_result_to_file("../../cpp_result_data.txt", results);
}

void test_performance(int iterations) {
    vector<vector<int>> loaded_data = read_data_from_file("../../test_data.txt");
    typedef chrono::high_resolution_clock clock;
    typedef chrono::milliseconds ms;
    typedef chrono::duration<float> fsec;

    auto start_time = clock::now();
    for (int i = 1; i < iterations; i++) {
        for (vector<int> test_set : loaded_data) {
            // Do nothing
        }
    }
    auto end_time = clock::now();
    fsec empty_time = end_time - start_time;
//    cout << "Empty Time: " << empty_time << " seconds" << endl;

    start_time = clock::now();
    for (int i = 1; i < iterations; i++) {
        for (vector<int> test_set : loaded_data) {
            median_low(test_set);
        }
    }
    end_time = clock::now();
    fsec execution_time = end_time - start_time - empty_time;
    cout << "Execution Time: " << execution_time << " seconds" << endl;
}

int main() {
//    test_correctness();
    for (int i = 1; i < 100; i++) {
        test_performance(10000);
    }
    return 0;
}

