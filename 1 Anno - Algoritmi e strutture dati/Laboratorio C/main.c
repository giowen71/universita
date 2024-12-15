#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


//definizione strutture dati
typedef char element_type;

typedef struct list_element{
    element_type value;
    struct list_element *next;
}item;

typedef item *list;

bool ricerca_elemento(list l, char value){
    while (l!=NULL){
        if (l->value==value)
            return true;
        l=l->next;
    }
    return false;
}
//print interattive
void showlist(list l) {
    printf("[");
    while (l!=NULL){
        putchar (l->value);
        l=l->next;
        if (l!=NULL)
            printf(",");
    }
    printf("]\n");
}

//print interna ricorsiva
void showr_list(list l){
    if(l!=NULL){
        putchar(l->value);
        if (l->next!=NULL){
            printf(",");
            showr_list(l->next);
        }
    }
}



//procedura ricorsiva
void showr_l (list l){
    printf("[");
    showr_list(l);
    printf("]\n");
}

void inserisce_davanti(){
    list root=NULL, aux;
    char n;
    while ((n=getchar())!='\n'){
        aux=(list)malloc(sizeof(struct list_element));
        aux->value=n;
        aux->next=root;
        root=aux;
    }
    showlist(root);
    showr_l(root);
}

list inserisci_lista(){
    list root=NULL, aux;
    char n;
    while ((n=getchar())!='\n'){
        aux=(list)malloc(sizeof(struct list_element));
        aux->value=n;
        aux->next=root;
        root=aux;
    }
    return root;
}


void inserisce_dietro() {
    list root = NULL, aux;
    char n;
    while ((n=getchar())!='\n'){
        if (root==NULL) {
            root=(list)malloc(sizeof(struct list_element));
            aux=root;
        }else{
            aux->next=(list)malloc(sizeof(struct list_element));
            aux=aux->next;
        }
        aux->value=n;
        aux->next=NULL;
    }
    showlist(root);
    showr_l(root);
}

int main(){
    system("cls");
    printf("Inserisci il primo set di volori equando hai finito premi return\n");
    //inserisce_davanti();
    //printf("Inserisci il secondo set di volori equando hai finito premi return\n");
    //inserisce_dietro();
    list l=inserisci_lista();
    bool ret=ricerca_elemento(l,'a');
    printf("%s",ret ? "true" : "false");
}