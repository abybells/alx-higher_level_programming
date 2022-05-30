#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a single linked list has a cycle
 * @list: a linked list
 * Return: 1 if succes, 0 on fail
 */

int check_cycle(listint_t *list)
{
	int i = 0;

	if (!list)
		return (0);
	while (list)
	{
		list = list->next;
		i++;
		if (i > 100)
			return (1);
	}
	return (0);
}
