#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_list - prints elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_list(const list_t *h)
{
    const list_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_node_end - e end of a list_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: new element or NULL if it fails
 */
list_t *add_node_end(list_t **head, const int n)
{
    list_t *new;
    list_t *current;

    current = *head;

    new = malloc(sizeof(list_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_list - frees a list_t list
 * @head: list to be freed
 * Return: void
 */
void free_list(list_t *head)
{
    list_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
