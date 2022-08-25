#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - This fucntion checks if there is cycle in
 * singly linked list
 * @list: Pointer to the head
 *
 * Return: 0 if there is no cycle and 1 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *check;
	listint_t *follow;

	if (!list)
		return (0);

	check = list;
	follow = list;
	while (check && follow && check->next)
	{
		follow = follow->next;
		check = check->next->next;
		if (check == follow)
			return (1);
	}
	return (0);

}
