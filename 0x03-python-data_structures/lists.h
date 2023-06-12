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
struct listint_s
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
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * void free_listint(listint_t *head);
 *
 * Description: frees all the nodes in a linked list
 *
 * Parameters:
 *   head - The head of the linked list
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
 */
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
