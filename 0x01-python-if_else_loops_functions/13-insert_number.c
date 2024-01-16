#include "lists.h"
#include <stdlib.h>

/**
 * insert_node -  singly linked list node insertion function
 * @head: first node
 * @num: the number to be inserted
 * Return: address
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
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
