#include "lists.h"

/**
  * insert_node - insert a number in a sorted linked list.
  * @head: a singly linked list.
  * @number: the number to insert.
  * Return: the address of the new node.
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current && current->next && (current->next)->n < number)
			current = current->next;
		if (current->n < number)
		{
			new->next = current->next;
			current->next = new;
		}
		else
		{
			new->next = current;
			*head = new;
		}
	}

	return (new);
}
