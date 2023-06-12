#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next;

	/* Find the middle node of the linked list */
	while (fast && fast->next)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}

	if (fast)  /* Odd number of nodes */
		slow = slow->next;

	/* Compare the first and second halves of the list */
	while (prev && slow)
	{
		if (prev->n != slow->n)
			return 0;
		prev = prev->next;
		slow = slow->next;
	}

	return 1;
}
