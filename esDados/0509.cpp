#include <iostream>

using namespace std;

int main()
{
    int n, aux, prod=1;

    cout << "Insira um número: ";
    cin >> n;

    for (aux = 1; aux <= n; aux++)
        prod *= aux;

    cout << "Fatorial: " << prod << endl;

    return 0;
}