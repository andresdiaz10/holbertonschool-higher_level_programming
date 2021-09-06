#include "lists.h"

/**
 * check_cycle - check a cycle of a linked list using de floyd algorithm
 * @list: linked list
 *
 * Return: 1 if is a cycle, otherwhise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slower;
	listint_t *faster;

	/* If only have one node no have cycle*/
	if (!(list) || !(list->next))
		return (0);
	/*Move one pointer*/
	slower = list->next;
	/*Move two pointers*/
	faster = list->next->next;
	while (slower && faster)
	{
		/* Check cycle */
		if (slower == faster)
			return (1);
		/* Move list */
		slower = slower->next;
		faster = faster->next->next;
	}
	return (0);
}
