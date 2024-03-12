#include "lists.h"
/**
  * check_cycle - check if list has a cycle
  * @list: address of first node
  * Return: 0 there's no cycle, 1 cycle exists
  */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	
	while (list->next != NULL)
	{
		if (list->next == first)
			return (1);
		list = list->next;
	}
	return (0);
}
