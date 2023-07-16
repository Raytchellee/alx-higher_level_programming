#include "lists.h"

/**
 * rev_linked_list - Reverses a singly-linked listint_t list.
 * @head: linked list head
 * Return: reversed list head
 */

listint_t *rev_linked_list(listint_t **head)
{
	listint_t *current = *head, *temp, *new_node = NULL;

	while (current)
	{
		temp = current->next;
		current->next = new_node;
		new_node = current;
		current = temp;
	}

	*head = new_node;
	return (*head);
}

/**
 * is_palindrome - Checks if singly linked list is palindrome.
 * @head: linked list head
 * Return: 1 if true, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *half, *reversed;
	size_t idx, length = 0, mid;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		length++;
		temp = temp->next;
	}

	temp = *head;
	mid = length / 2;
	for (idx = 0; idx < mid - 1; idx++)
		temp = temp->next;
	if ((length % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	reversed = rev_linked_list(&temp);
	half = reversed;

	temp = *head;
	while (reversed)
	{
		if (temp->n != reversed->n)
			return (0);
		temp = temp->next;
		reversed = reversed->next;
	}
	rev_linked_list(&half);

	return (1);
}
