#include "lists.h"
#include <stdio.h>

/**
  * check_cycle - checks for cycles in singly linked lists.
  * @list: a singly linked list structure.
  * Return: 0 if there is no cycle 1 otherwise.
  */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list;
	listint_t *rapit = list;

	if (!list)
		return (0);
	while (rapit && rapit->next && (rapit->next)->next)
	{
		turtle = (turtle->next)->next;
		rapit = ((rapit->next)->next)->next;
		if (turtle == rapit)
			return (1);
	}
	return (0);
}
