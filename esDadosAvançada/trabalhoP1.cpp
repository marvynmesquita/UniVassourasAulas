#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;
};

Node* createNode(int data) {
    Node* newNode = new Node();
    if (!newNode) {
        cout << "Erro ao alocar memória!" << endl;
        return NULL;
    }
    newNode->data = data;
    newNode->left = newNode->right = NULL;
    return newNode;
}

Node* insertNode(Node* root, int data) {
    if (root == NULL) {
        root = createNode(data);
        return root;
    }
    if (data < root->data) {
        root->left = insertNode(root->left, data);
    } else if (data > root->data) {
        root->right = insertNode(root->right, data);
    }
    return root;
}

Node* findMin(Node* root) {
    while (root->left != NULL) {
        root = root->left;
    }
    return root;
}

Node* deleteNode(Node* root, int data) {
    if (root == NULL) {
        return root;
    } else if (data < root->data) {
        root->left = deleteNode(root->left, data);
    } else if (data > root->data) {
        root->right = deleteNode(root->right, data);
    } else {
        if (root->left == NULL && root->right == NULL) {
            delete root;
            root = NULL;
        } else if (root->left == NULL) {
            Node* temp = root;
            root = root->right;
            delete temp;
        } else if (root->right == NULL) {
            Node* temp = root;
            root = root->left;
            delete temp;
        } else {
            Node* temp = findMin(root->right);
            root->data = temp->data;
            root->right = deleteNode(root->right, temp->data);
        }
    }
    return root;
}

void preOrderTraversal(Node* root) {
    if (root == NULL) {
        return;
    }
    cout << root->data << " ";
    preOrderTraversal(root->left);
    preOrderTraversal(root->right);
}

void inOrderTraversal(Node* root) {
    if (root == NULL) {
        return;
    }
    inOrderTraversal(root->left);
    cout << root->data << " ";
    inOrderTraversal(root->right);
}

void postOrderTraversal(Node* root) {
    if (root == NULL) {
        return;
    }
    postOrderTraversal(root->left);
    postOrderTraversal(root->right);
    cout << root->data << " ";
}

void printTree(Node* root, string indent, bool last) {
    if (root != NULL) {
        cout << indent;
        if (last) {
            cout << "└─";
            indent += "  ";
        } else {
            cout << "├─";
            indent += "| ";
        }
        cout << root->data << endl;
        printTree(root->left, indent, false);
        printTree(root->right, indent, true);
    }
}

int main() {
    Node* root = NULL;
    int choice, data;

    do {
        cout << "Menu:" << endl;
        cout << "1. Inserir nó" << endl;
        cout << "2. Remover nó" << endl;
        cout << "3. Mostrar árvore" << endl;
        cout << "4. Buscar dado na árvore" << endl;
        cout << "5. Mostrar árvore (Pré-ordem)" << endl;
        cout << "6. Mostrar árvore (Pós-ordem)" << endl;
        cout << "7. Mostrar árvore (In-ordem)" << endl;
        cout << "8. Representar árvore com diagrama de barras" << endl;
        cout << "9. Sair" << endl;
        cout << "Escolha uma opção: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Digite o valor do nó a ser inserido: ";
                cin >> data;
                root = insertNode(root, data);
                break;
            case 2:
                cout << "Digite o valor do nó a ser removido: ";
                cin >> data;
                root = deleteNode(root, data);
                break;
            case 3:
                cout << "Árvore: ";
                printTree(root, "", true);
                break;
            case 4:
                cout << "Digite o valor a ser buscado: ";
                cin >> data;
                // Implementar busca na árvore
                break;
            case 5:
                cout << "Árvore (Pré-ordem): ";
                preOrderTraversal(root);
                cout << endl;
                break;
            case 6:
                cout << "Árvore (Pós-ordem): ";
                postOrderTraversal(root);
                cout << endl;
                break;
            case 7:
                cout << "Árvore (In-ordem): ";
                inOrderTraversal(root);
                cout << endl;
                break;
            case 8:
                // Implementar representação com diagrama de barras
                break;
            case 9:
                cout << "Encerrando o programa..." << endl;
                break;
            default:
                cout << "Opção inválida!" << endl;
                break;
        }
    } while (choice != 9);

    return 0;
}