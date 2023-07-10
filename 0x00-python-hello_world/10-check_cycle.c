#include <stdio.h>
#include "lists.h"

/*
 * check_cycle - checks for cycle in a lsit
 * @list: input list
 * Return: 1 if yes, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	int seen = 0;
	listint_t *slow = list, *fast = list;

	while (slow && slow->next)
	{
		fast = slow->next;

		while (fast->next)
		{
			if (fast == slow)
				return 1;

			fast = fast->next;
		}

		slow = slow->next;
	}

	return seen;
}
