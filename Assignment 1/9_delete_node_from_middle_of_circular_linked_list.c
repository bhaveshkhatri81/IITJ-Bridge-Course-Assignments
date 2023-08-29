#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

void insertEnd(struct Node** head, int data) {
    struct Node* newNode = createNode(data);

    if (*head == NULL) {
        *head = newNode;
        newNode->next = *head;
    } else {
        struct Node* current = *head;
        while (current->next != *head) {
            current = current->next;
        }
        current->next = newNode;
        newNode->next = *head;
    }
}

void deleteMiddle(struct Node** head) {
    if (*head == NULL) {
        printf("List is empty.\n");
        return;
    }

    struct Node* slow = *head;
    struct Node* fast = *head;
    struct Node* prev = NULL;

    while (fast != *head && fast->next != *head) {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    // If the number of nodes is even, move slow to the previous node
    if (fast == *head) {
        slow = prev;
    }

    // Delete the middle node
    if (slow == *head) {
        *head = (*head)->next;
    } else {
        prev->next = slow->next;
    }

    free(slow);
}

void display(struct Node* head) {
    if (head == NULL) {
        printf("List is empty.\n");
        return;
    }

    struct Node* current = head;

    do {
        printf("%d -> ", current->data);
        current = current->next;
    } while (current != head);

    printf("Head\n");
}

int main() {
    struct Node* head = NULL;
    insertEnd(&head, 10);
    insertEnd(&head, 20);
    insertEnd(&head, 30);
    insertEnd(&head, 40);
    insertEnd(&head, 50);

    printf("Original Circular Linked List:\n");
    display(head);

    deleteMiddle(&head);

    printf("Circular Linked List after deleting the middle node:\n");
    display(head);

    return 0;
}
