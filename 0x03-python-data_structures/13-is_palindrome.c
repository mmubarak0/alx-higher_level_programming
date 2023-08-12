#include "lists.h"

/**
  * is_palindrome - checks if a singly linked list is a palindrome.
  * @head: the first node of a singly linked list.
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
  */
int is_palindrome(listint_t **head)
{
	listint_t *list_head = *head;
	listint_t *list_tail = *head;
	listint_t *new;
	listint_t *current;
	listint_t *prev = NULL, *next = NULL;
	int n = 0, i, d;

	if (!*head)
		return (1);
	new = NULL;
	while (list_tail)
	{
		n++;
		add_nodeint_end(&new, list_tail->n);
		list_tail = list_tail->next;
	}
	current = new;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	list_tail = prev;
	i = 0;
	d = n / 2;
	while (i++ <= d)
	{
		if (list_head->n != list_tail->n)
		{
			free_listint(prev);
			return (0);
		}
		list_head = list_head->next;
		list_tail = list_tail->next;
	}
	free_listint(prev);
	return (1);
}
