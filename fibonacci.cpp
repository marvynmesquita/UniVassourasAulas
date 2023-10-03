#include <iostream>
using namespace std;

void fibonacci(int n) {
    int first = 0, second = 1, next;

    cout << "Sequencia de Fibonacci ate " << n << ": \n ";

    while (first <= n) {
        cout << first << " ";

        next = first + second;
        first = second;
        second = next;
    }
}

int main() {
    int num;

    cout << "Digite um numero: ";
    cin >> num;

    fibonacci(num);

    return 0;
}