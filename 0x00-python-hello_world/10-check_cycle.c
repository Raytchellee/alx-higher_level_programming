#include <stdio.h>
#include "lists.h"

/**
 *check_cycle - checks for cycle in a lsit
 *@list: input list
 *Return: 1 if yes, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	int seen = 0;
	listint_t *slow = list, *fast = list;

	while (slow && fast && slow->next)
	{
		slow = slow->next;

		if (fast->next || fast->next->next)
			fast = fast->next->next;
		else
			break;

		if (fast == slow)
		{
			seen = 1;
			break;
		}
	}

	return (seen);
}
