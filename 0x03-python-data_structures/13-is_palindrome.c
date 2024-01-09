#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * add_nodeint - add a new node at the beginning of listint list
 * @head: pointer to the head of the list
 * @n: integer
 * Return: NULL if failed
 */
/**listint_t *add_nodeint(listint_t **head, const int n)
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
*/
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;
	
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return *head;
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
	listint_t *second_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast != NULL)
		slow = slow->next;
	second_half = reverse_listint(&slow);

	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
			return (0);

		*head = (*head)->next;
		second_half = second_half->next;
	}

	reverse_listint(&slow);

	return (1);
}
