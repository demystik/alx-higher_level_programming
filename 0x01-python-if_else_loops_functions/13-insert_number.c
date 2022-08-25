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
	listint_t *ins;
	listint_t *ptr;

	ptr = *head;

	ins = malloc(sizeof(listint_t));
	if (ins == NULL)
		return (NULL);
	ins->n = number;

	if (ptr == NULL || ptr->n >= number)
	{
		ins->next = ptr;
		*head = ins;
		return (ins);
	}
	
	while (ptr && ptr->next &&  ptr->next->n < number)
		ptr = ptr->next;

	ins->next = ptr->next;
	ptr->next = ins;

return (ins);
}
