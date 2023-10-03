#include <iostream>
#include <vector>

int main() {
    std::vector<std::vector<int>> matriz1 = {{1,2,3}, {4,5,6}, {7,8,9}};
    std::vector<std::vector<int>> matriz2 = {{9,7,8}, {6,5,4}, {3,2,1}};
    std::vector<std::vector<int>> resultado(matriz1.size(), std::vector<int>(matriz1[0].size()));

    for (int i = 0; i < matriz1.size(); i++) {
        for (int j = 0; j < matriz1[i].size(); j++){
            resultado[i][j] = matriz1[i][j] + matriz2[i][j];
        }
    }

    for (const auto& linha : resultado){
        for (const auto& elemento : linha){
            std::cout << elemento << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}