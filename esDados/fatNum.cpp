#include <iostream>

int main() {
    int num, fatorial = 1;

    std::cout << "Digite um número: ";
    std::cin >> num;

    for (int i = 1; i <= num; i++){
        fatorial *= i;
    }

    std::cout << "O fatorial de " << num << " é: " << fatorial << std::endl;

    return 0;
}