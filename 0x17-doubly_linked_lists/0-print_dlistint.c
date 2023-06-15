#include <stdio.h>
#include "lists.h"
/**
 * size_t count - Variable to count the number of nodes
 * @h: Traverse the list
 * @h->n: Print the current node's value
 * @h->next: MOve to the next node
 * count++ Increment the node count
 * return = count
 */

size_t print_dlistint(const dlistint_t *h)
{
    size_t count = 0;
	while (h != NULL)
	{
        printf("%d\n", h->n);
	h = h->next;
	count++;
    	}

    return count;
}
