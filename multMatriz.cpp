#include <iostream>
using namespace std;

int main() {
    int matriz1[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}};
    int matriz2[3][3] = {{9,8,7}, {6,5,4}, {3,2,1}};
    int resultado[3][3];

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++){
            resultado[i][j] = 0;
            for (int k = 0; k < 3; k++){
                resultado[i][j] = matriz1[i][j] * matriz2[k][j];
            }
        }
    }

    for (const auto& linha : resultado){
        for (const auto& elemento : linha){
            cout << elemento << " ";
        }
        cout << endl;
    }
    return 0;
}