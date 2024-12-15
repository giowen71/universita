#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
    struct node *parent;
};

struct node *root = NULL;

struct node* create_node(int data, struct node *parent) {
    struct node *new_node = (struct node *)malloc(sizeof(struct node));
    new_node->data = data;
    new_node->left = NULL;
    new_node->right = NULL;
    new_node->parent = parent;
    return new_node;
}

void insert(struct node **root, int data) {
    if (*root == NULL) {
        *root = create_node(data, NULL);
    } else {
        struct node *temp = *root;
        if (data <= temp->data) {
            if (temp->left == NULL) {
                temp->left = create_node(data, temp);
            } else {
                insert(&temp->left, data);
            }
        } else {
            if (temp->right == NULL) {
                temp->right = create_node(data, temp);
            } else {
                insert(&temp->right, data);
            }
        }
    }
}

int main() {
    insert(&root, 12);
    insert(&root, 5);
    insert(&root, 20);
    insert(&root, 25);
    insert(&root, 1);
    insert(&root, 13);
    insert(&root, 105);
    

    printf("Root: %d\n", root->data);
    printf("Left child: %d\n", root->left->data);
    printf("Right child: %d\n", root->right->data);

    return 0;
}
