#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

// Structure for a node in the linked list
typedef struct ListNode {
    int val;
    struct ListNode* next;
} ListNode;

// Function to check if a singly linked list is a palindrome
int is_palindrome(ListNode** head) {
    // Empty list is considered a palindrome
    if (*head == NULL) {
        return 1;
    }
    
    // Find the middle node of the list
    ListNode* slow = *head;
    ListNode* fast = *head;
    
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }
    
    // Reverse the second half of the list
    ListNode* prev = NULL;
    ListNode* curr = slow;
    
    while (curr != NULL) {
        ListNode* next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    
    // Compare the first half and the reversed second half of the list
    ListNode* firstHalf = *head;
    ListNode* secondHalf = prev;
    
    while (secondHalf != NULL) {
        if (firstHalf->val != secondHalf->val) {
            return 0;  // Not a palindrome
        }
        firstHalf = firstHalf->next;
        secondHalf = secondHalf->next;
    }
    
    return 1;  // It is a palindrome
}

// Helper function to create a new node with a given value
ListNode* createNode(int value) {
    ListNode* newNode = (ListNode*)malloc(sizeof(ListNode));
    newNode->val = value;
    newNode->next = NULL;
    return newNode;
}

// Helper function to insert a new node at the beginning of the list
void insertAtBeginning(ListNode** head, int value) {
    ListNode* newNode = createNode(value);
    newNode->next = *head;
    *head = newNode;
}

// Test the is_palindrome function
int main() {
    // Create a sample linked list: 1 -> 2 -> 3 -> 2 -> 1
    ListNode* head = NULL;
    insertAtBeginning(&head, 1);
    insertAtBeginning(&head, 2);
    insertAtBeginning(&head, 3);
    insertAtBeginning(&head, 2);
    insertAtBeginning(&head, 1);
    
    // Check if the linked list is a palindrome
    int result = is_palindrome(&head);
    
    if (result == 1) {
        printf("The linked list is a palindrome.\n");
    } else {
        printf("The linked list is not a palindrome.\n");
    }
    
    // Free the memory
    ListNode* current = head;
    while (current != NULL) {
        ListNode* temp = current;
        current = current->next;
        free(temp);
    }
    
    return 0;
}
