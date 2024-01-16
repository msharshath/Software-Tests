#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <limits>
#include <chrono>
#include <thread>

bool isValidFloatingPoint(const std::string& input) {
    std::istringstream iss(input);
    double test;
    char leftover;

    // Attempt to read a double followed by any remaining characters
    if (iss >> test && !(iss >> leftover)) {
        // Check if the input contains a decimal point
        return (input.find('.') != std::string::npos);
    }

    return false;
}

int main() {
    // Variable declaration
    double total_sum = 0.0;
    int count = 0;

    // Continuous input loop
    while (true) {
        // Get a new value from the user
        std::string input_value;
        std::cout << "Enter a floating-point number (or 'x' to end): ";
        std::getline(std::cin, input_value);

        // Check if the user wants to end the input
        if (input_value == "x") {
            std::cout << "Exiting the program." << std::endl;
            break;
        }

        // Validate the input
        if (!isValidFloatingPoint(input_value)) {
            std::cerr << "Invalid input: Please enter a valid floating-point number." << std::endl;
            continue;
        }

        try {
            // Convert input to a double
            double new_value = std::stod(input_value);

            // Update variables
            total_sum += new_value;
            count++;

            // Calculate and display the current mean
            double current_mean = total_sum / count;
            std::cout << "Current mean: " << std::fixed << std::setprecision(3) << current_mean << std::endl;

        } catch (const std::invalid_argument& e) {
            std::cerr << "Invalid input: " << e.what() << std::endl;
        }
    }

    // Display the final mean value
    double final_mean = (count > 0) ? total_sum / count : 0.0;
    std::cout << "Final mean value: " << std::fixed << std::setprecision(2) << final_mean << std::endl;

    // Introduce a delay before exiting (e.g., 5 seconds)
    std::this_thread::sleep_for(std::chrono::seconds(5));

    return 0;
}