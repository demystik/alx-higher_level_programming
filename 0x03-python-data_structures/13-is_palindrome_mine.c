#include "lists.h"
/**
 * is_palindrome - This function checks if a singly
 * list is palindrome
 * @head: pointer to the head node
 *
 * Return: 0 if it is not and 1 if it is
 */
int is_palindrome(listint_t **head)
{
	int i, j, k;
	int bol = 0;
	listint_t *ptr;
	listint_t *loop;

	ptr = *head;
	loop = ptr;
	i = 0;
	j = 0;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (ptr != NULL)
	{
		ptr = ptr->next;
		i++;
	}
	int arr[i];

	while (loop != NULL)
	{
		arr[j] = loop->n;
		j++;
		loop = loop->next;
	}
	j = sizeof(arr) / sizeof(int);
	j--;
	k = j;
	i = 0;
	while (i <= k)
	{
		/* printf("i si %d and j is %d\n", arr[i], arr[j]); */
		if (arr[i] != arr[j])
			bol = 1;
		i++, j--;
	}

	if (bol == 1)
		return (0);
return (1);
}
