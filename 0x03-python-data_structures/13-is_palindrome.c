#include "lists.h"

/**
  * push - push value to stack.
  * @s: stack struct.
  * @value: value to push.
  */
void push(stack *s, int value)
{
	if (s->top == MAX_SIZE - 1)
		return; /* stack is full */
	s->n[++(s->top)] = value;
}

/**
  * pop - pop value from stack.
  * @s: stack struct.
  * Return: value popped.
  */
int pop(stack *s)
{
	if (s->top == -1)
		return (-1); /* stack is empty */
	return (s->n[(s->top)--]);
}

/**
  * peek - element at the peek of stack.
  * @s: stack struct.
  * Return: value of peek.
  */
int peek(stack *s)
{
	if (s->top == -1)
		return (-9999999);
	return (s->n[s->top]);
}

/**
  * is_palindrome - checks if a singly linked list is a palindrome.
  * @head: the first node of a singly linked list.
  * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
  */
int is_palindrome(listint_t **head)
{
	listint_t *list_head = *head;
	stack s;
	int len, half_len, i = 0;

	s.top = -1;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	for (len = 0; list_head; len++)
		list_head = list_head->next;
	half_len = len / 2;
	list_head = *head;
	while (list_head)
	{
		if (peek(&s) != list_head->n)
		{
			push(&s, list_head->n);
			if (len % 2 != 0 && i == half_len)
				pop(&s);
		}
		else
			pop(&s);
		list_head = list_head->next;
		i++;
	}
	if (peek(&s) == -9999999)
		return (1);
	return (0);
}
