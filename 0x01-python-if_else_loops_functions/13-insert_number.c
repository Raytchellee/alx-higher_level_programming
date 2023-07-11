#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts node
 * @number: node number
 * Return: address of the returned node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = NULL, *curr_node, *returned;

	if (head == NULL)
		return (NULL);
	curr_node = *head;

	while (curr_node != NULL)
	{
		if (curr_node->n > number)
		{
			returned = malloc(sizeof(listint_t));

			if (returned == NULL)
				return (NULL);
			if (node != NULL)
				node->next = returned;
			returned->next = curr_node;

			if (curr_node == *head)
				*head = returned;
			returned->n = number;
			return (returned);
		}
		node = curr_node;
		curr_node = curr_node->next;
	}

	returned = malloc(sizeof(listint_t));
	if (returned == NULL)
		return (NULL);
	if (*head == NULL)
		*head = returned;
	else
		node->next = returned;
	returned->next = NULL;
	returned->n = number;

	return (returned);
}
