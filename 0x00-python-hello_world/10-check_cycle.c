#include "lists.h"
/**
 * check_cycle - checks if a linked list contain a cycle
 * @list: linked list
 *
 * Return: 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
