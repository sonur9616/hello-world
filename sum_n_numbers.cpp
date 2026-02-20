#include <iostream>
#include <limits>

long long sum_upto_n(long long n) {
    return n * (n + 1) / 2;
}

int main() {
    std::cout << "Enter a number: ";

    long long n{};
    if (!(std::cin >> n)) {
        std::cout << "Invalid input\n";
        return 1;
    }

    if (n <= 0) {
        std::cout << "Please enter a positive integer\n";
        return 1;
    }

    __int128 raw_sum = static_cast<__int128>(n) * (n + 1) / 2;
    if (raw_sum > std::numeric_limits<long long>::max()) {
        std::cout << "Number is too large\n";
        return 1;
    }

    std::cout << "Sum: " << sum_upto_n(n) << '\n';
    return 0;
}
