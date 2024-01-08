#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * add_nodeint - add a new node at the beginning of listint list
 * @head: pointer to the head of the list
 * @n: integer
 * Return: NULL if failed
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (new);
}
/**
 * is_palindrome - identify if single linked
 * @head: pointer
 * Return: 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *stack = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		add_nodeint(&stack, slow->n);
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
		slow = slow->next;

	while (slow != NULL)
	{
		if (slow->n != stack->n)
		{
			free_listint(stack);
			return (0);
		}
		slow = slow->next;
		stack = stack->next;
	}

	free_listint(stack);
	return (1);
}
