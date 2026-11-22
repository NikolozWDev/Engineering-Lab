#include <algorithm>
#include <iostream>
#include <string>

int main() {
    std::string s = "engineering lab";
    std::reverse(s.begin(), s.end());
    std::cout << s << "\n";
}
