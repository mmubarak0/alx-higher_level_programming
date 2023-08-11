#include "lists.h"

/**
  * rev - reverse a singly linked list.
  * @p: first node of the list.
  */
void rev(listint_t *p)
{
	listint_t *current = p;
	listint_t *prev = NULL, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	p = prev;
}

/**
  * is_palindrome - checks if a singly linked list is a palindrome.
  * @head: the first node of a singly linked list.
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
  */
int is_palindrome(listint_t **head)
{
	listint_t *list_head = *head;
	listint_t *list_tail = *head;

	if (!*head)
		return (1);
	rev(list_tail);
	while (list_head)
	{
		if (list_head->n != list_tail->n)
			return (0);
		list_head = list_head->next;
		list_tail = list_tail->next;
	}
	return (1);
}
