#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - This function insert number into
 * a sorted singly linked list
 * @head: The pointer to the head node
 * @number: integer to assign to the inserted node
 *
 * Return: address of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *i;
	listint_t *ins;
	listint_t *ptr;
	listint_t *follow;

	int n;
	
	if (!*head)
		return (NULL);
	i = *head;
	ptr = *head;
	n = 1;

	while(i->next != NULL)
	{
		i = i->next;
		n++;
	}
	if (n % 2 == 1)
		n--;
	n = n/2;
	ins = malloc(sizeof(listint_t));
	if (ins == NULL)
		return (NULL);

	while(n != 1)
	{
		ptr = ptr->next;
		n--;
	}
	follow = ptr->next;
	ptr->next = ins;
	ins->n = number;
	ins->next = follow;

return (ins);
}
