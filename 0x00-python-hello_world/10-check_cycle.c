#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 (has a cycle), 0 (no cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *h = list;

	if (!list)
		return (0);

	while (s && h && h->next)
	{
		s = s->next;
		h = h->next->next;
		if (s == h)
			return (1);
	}

	return (0);
}
