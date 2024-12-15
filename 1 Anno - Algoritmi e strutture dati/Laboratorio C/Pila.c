#include <stdio.h>
#include <stdbool.h>
#include <limits.h> // Per INT_MIN

#define MAX_SIZE 10
int stack[MAX_SIZE];
int top = -1;

bool isEmpty() {
    return top == -1;
}

bool isFull() {
    return top == MAX_SIZE - 1;
}

int peek() {
    if (isEmpty()) {
        printf("Pila Vuota\n");
        return INT_MIN; // Restituisce un valore speciale per indicare errore
    }
    return stack[top];
}

void push(int value) {
    if (isFull()) {
        printf("Pila Full\n");
        return;
    }
    top++;
    stack[top] = value;
}

int pop() {
    if (isEmpty()) {
        printf("Pila Vuota\n");
        return INT_MIN; // Restituisce un valore speciale per indicare errore
    }
    int value = stack[top];
    top--;
    return value;
}

int main() {
    push(1);
    push(2);
    push(3);

    int value = peek();
    if (value != INT_MIN) {
        printf("Top: %d\n", value);
    }

    while (!isEmpty()) {
        printf("Pop: %d\n", pop());
    }

    // Tentativo di pop su una pila vuota
    value = pop();
    if (value == INT_MIN) {
        printf("Errore: Tentativo di rimuovere da una pila vuota.\n");
    }

    return 0;
}
