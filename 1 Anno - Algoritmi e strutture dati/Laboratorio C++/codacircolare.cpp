#include <iostream>
#include <vector>

#define MAX_SIZE 10

int queue[MAX_SIZE];
int front = 0;
int rear = -1;
int item_count = 0;

void enqueue(int data) {
    if (item_count == MAX_SIZE) {
        std::cout << "Error: Queue Overflow\n";
    } else {
        std::cout << "E' entrata una persona\n";
        rear = (rear + 1) % MAX_SIZE;
        queue[rear] = data;
        item_count++;
    }
}

int dequeue() {
    if (item_count == 0) {
        std::cout << "Error: Queue underflow\n";
        return -1;
    } else {
        std::cout << "Va via una persona\n";
        int data = queue[front];
        front = (front + 1) % MAX_SIZE;
        item_count--;
        return data;
    }
}

void print_queue() {
    if (item_count == 0) {
        std::cout << "Error: Queue is empty\n";
    } else {
        for (int i = 0; i < item_count; i++) {
            int index = (front + i) % MAX_SIZE;
            std::cout << queue[index] << std::endl;
        }
    }
}

int main() {
    enqueue(1);
    enqueue(2);
    enqueue(3);
    enqueue(4);

    std::cout << "Queue elements\n";
    print_queue();
    dequeue();
    dequeue();

    std::cout << "Queue elements\n";
    print_queue();
    dequeue();
    dequeue();
    dequeue();
    dequeue();

    return 0;
}
