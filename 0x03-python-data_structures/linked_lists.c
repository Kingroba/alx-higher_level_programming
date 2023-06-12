#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
  int n;
  struct listint_s *next;
};

/**
 * size_t print_listint(const listint_t *h);
 *
 * Description: prints the values of all the nodes in a linked list
 *
 * Parameters:
 *   h - The head of the linked list
 *
 * Returns:
 *   The number of nodes in the linked list
 *
 * Comments:
 *   This function iterates over all the nodes in the linked list and prints their values.
 */
size_t print_listint(const listint_t *h);

/**
 * listint_t *add_nodeint_end(listint_t **head, const int n);
 *
 * Description: adds a new node to the end of a linked list
 *
 * Parameters:
 *   head - A pointer to the head of the linked list
 *   n - The value of the new node
 *
 * Returns:
 *   A pointer to the new node
 *
 * Comments:
 *   This function allocates a new node and initializes its values. The new node is then added to the end of the linked list.
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * void free_listint(listint_t *head);
 *
 * Description: frees all the nodes in a linked list
 *
 * Parameters:
 *   head - The head of the linked list
 *
 * Comments:
 *   This function iterates over all the nodes in the linked list and frees them.
 */
void free_listint(listint_t *head);

/**
 * int is_palindrome(listint_t **head);
 *
 * Description: checks if a linked list is a palindrome
 *
 * Parameters:
 *   head - A pointer to the head of the linked list
 *
 * Returns:
 *   1 if the linked list is a palindrome, 0 otherwise
 *
 * Comments:
 *   This function checks if a linked list is a palindrome by comparing the values of the nodes in the list from the beginning to the end.
 */
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
