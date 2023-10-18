#include <iostream>
#define MAX_SIZE 100

using namespace std;

class Queue {
    private:
        int front, rear;
        int queue[MAX_SIZE];
    public:
        Queue() {
            front = -1;
            rear = -1;
        }
        bool isFull() {
            return (rear == MAX_SIZE - 1);
        }
        bool isEmpty() {
            return (front == -1 && rear == -1);
        }

        void enqueue(int data) {
            if (isFull()) {
                cout << "A fila está cheia." << endl;
                return;
            } else if (isEmpty()) {
                front = rear = 0;
            } else {
                rear++;
            }

            queue[rear] = data;
            cout << "Cliente com o número " << data " entrou na fila." << endl;
        }

        void dequeue() {
            if (isEmpty()) {
                cout << "A fila está vazia." << endl;
            } else if (front == rear) {
                cout << "Cliente com o número " << queue[front] << " saiu da fila." << endl;
                front = rear = -1;
            } else {
                cout << "Cliente com o número " << queue[front] << " saiu da fila." << endl;
                front++;
            }
        }

        void display() {
            if (isEmpty()) {
                cout << "A fila está vazia." << endl;
                return;
            }
            cout << "Fila de clientes: ";
            for (int i = front; i <= rear; i++) {
                cout << queue[i] << " "
            }
            cout << endl;
        }
}

int main() {
    Queue queue;
    int choice, data;

    do {
        cout << "Escolha uma opção:" << endl;
        cout << "1. Entrar na fila" << endl;
        cout << "2. Sair da fila" << endl;
        cout << "3. Mostrar a fila" << endl;
        cout << "0. Sair do programa" << endl;
        
        cin >> choice;

        switch(choice) {
            case 1:
                cout << "Digite o número do cliente: ";
                cin >> data;
                queue.enqueue(data);
                break;
            case 2:
                queue.dequeue();
                break;
            case 3:
                queue.display();
                break;
            case 0:
                cout << "Encerrando o programa." << endl;
                break;
            default:
                cout << "Opção inválida." << endl;
        }

        cout << endl;
    }   while (choice != 0);

    return 0;
}