#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> lista = {1,2,3,4,5};

    std::reverse(lista.begin(), lista.end());

    for (const auto& elemento : lista) {
        std::cout << elemento << " ";
    }

    return 0;
}