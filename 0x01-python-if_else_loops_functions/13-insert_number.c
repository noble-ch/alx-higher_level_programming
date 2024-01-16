#include "lists.h"
#include <stdlib.h>

/**
 * insert_node -  singly linked list node insertion function
 * @head: first node
 * @num: the number to be inserted
 * Return: address
 */
list_t *insert_node(list_t **head, int num)
{
	list_t *new;
	list_t *current;

	current = *head;

	new = malloc(sizeof(list_t));
	if (new == NULL)
		return (NULL);

	new->n = num;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > num)
				break;

			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
