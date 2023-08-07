#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - checks for cycles in singly linked lists.
  * @list: a singly linked list structure.
  * Return: 0 if there is no cycle 1 otherwise.
  */
int check_cycle(listint_t *list)
{
	listint_t *p = list;

	if (!p)
		return (0);
	p = p->next;
	while (p)
	{
		if (p < p->next)
			return (1);
		p = p->next;
	}
	return (0);
}
