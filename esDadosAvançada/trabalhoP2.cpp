#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <sstream>

// Função para verificar se existe um caminho entre v e w
bool existeCaminho(std::vector<std::vector<int> >& grafo, int v, int w) {
    std::vector<bool> visitado(grafo.size(), false);
    std::queue<int> fila;
    fila.push(v);
    visitado[v] = true;

    while (!fila.empty()) {
        int atual = fila.front();
        fila.pop();

        if (atual == w) return true;

        for (int vizinho : grafo[atual]) {
            if (!visitado[vizinho]) {
                fila.push(vizinho);
                visitado[vizinho] = true;
            }
        }
    }
    return false;
}

int main() {
    std::ifstream arquivo("grafo.txt");
    std::string linha;
    int numVertices;

    // Lendo o número de vértices
    std::getline(arquivo, linha);
    std::istringstream(linha) >> numVertices;

    // Lendo a lista de vértices
    std::getline(arquivo, linha);
    std::istringstream verticesStream(linha);
    std::vector<int> vertices(numVertices);
    for (int& vertice : vertices) verticesStream >> vertice;

    // Inicializando o grafo
    std::vector<std::vector<int> > grafo(numVertices);
    while (std::getline(arquivo, linha)) {
        int v, w;
        std::istringstream arestaStream(linha);
        arestaStream >> v >> w;
        grafo[v].push_back(w);
    }

    // Menu para receber os vértices v e w
    int v, w;
    std::cout << "Digite o vértice v: ";
    std::cin >> v;
    std::cout << "Digite o vértice w: ";
    std::cin >> w;

    // Verificando se existe um caminho de v a w
    if (existeCaminho(grafo, v, w)) {
        std::cout << "Existe um caminho de " << v << " a " << w << ".\n";
    } else {
        std::cout << "Não existe um caminho de " << v << " a " << w << ".\n";
    }

    return 0;
}
