#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        printf("Memory allocation failed.");
        exit(1);
    }
    newNode->data = data;
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}

void insertAtEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        struct Node* current = *head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
        newNode->prev = current;
    }
}

void deleteFromPosition(struct Node** head, int position) {
    if (*head == NULL) {
        printf("Cannot delete from an empty list.");
        return;
    }

    if (position == 1) {
        struct Node* temp = *head;
        *head = (*head)->next;
        if (*head != NULL) {
            (*head)->prev = NULL;
        }
        free(temp);
        return;
    }

    int count = 1;
    struct Node* current = *head;
    while (current != NULL && count < position) {
        current = current->next;
        count++;
    }

    if (current == NULL) {
        printf("Invalid position to delete.");
        return;
    }

    if (current->next != NULL) {
        current->next->prev = current->prev;
    }

    if (current->prev != NULL) {
        current->prev->next = current->next;
    }

    free(current);
}

void display(struct Node* head) {
    if (head == NULL) {
        printf("Doubly Linked List is empty.");
        return;
    }

    struct Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    struct Node* head = NULL;

    insertAtEnd(&head, 10);
    insertAtEnd(&head, 20);
    insertAtEnd(&head, 30);
    insertAtEnd(&head, 40);
    insertAtEnd(&head, 50);

    printf("Doubly Linked List before deletion:\n");
    display(head);

    int positionToDelete = 3;
    deleteFromPosition(&head, positionToDelete);

    printf("\nDoubly Linked List after deletion from position %d:\n", positionToDelete);
    display(head);

    return 0;
}
