#include "lists.h"

/**
 * insert_node_helper - helps insert_node function 
 * @head: pointer to the head of the linked list
 * @number: number to add to the sorted linked list
 * Return: newly created node or null it there is no any
 */

listint_t *insert_node_helper(listint_t **head, int number, listint_t **tmp2)
{
	*tmp2 = malloc(sizeof(listint_t));
	if (*tmp2 == NULL)
		return (NULL);
	(*tmp2)->n = number;

	if (*head == NULL)
	{
		(*tmp2)->next = NULL;
		*head = *tmp2;
		return (*tmp2);
	}
	else if ((*head)->n > number)
	{
		(*tmp2)->next = *head;
		*head = *tmp2;
		return (*tmp2);
	}
	else if ((*head)->next == NULL)
	{
		(*tmp2)->next = NULL;
		(*head)->next = *tmp2;
		return (*tmp2);
	}
	else
	{
		free(*tmp2);
		*tmp2 = NULL;
	}
	return (*tmp2);
}

/**
 * insert_node - iserts node to the sorted linked list
 * @head: pointer to the head of the linked list
 * @number: number to add to the sorted linked list
 * Return: newly created node or null if there is none created
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp1;

	insert_node_helper(head, number, &tmp2);
	if (tmp2 != NULL)
		return (tmp2);

	tmp1 = *head;
	while (tmp1 != NULL)
	{
		if (tmp1->next->n < number)
		{
			tmp1 = tmp1->next;
			if (tmp1->next  == NULL)
			{
				listint_t *tmp2;

				tmp2 = malloc(sizeof(listint_t));
				if (tmp2 == NULL)
					return (NULL);
				tmp2->n = number;
				tmp2->next = NULL;
				tmp1->next = tmp2;
				return (tmp2);
			}
		}
		else
		{
			listint_t *tmp2;

			tmp2 = malloc(sizeof(listint_t));
			if (tmp2 == NULL)
				return (NULL);
			tmp2->n = number;
			tmp2->next = tmp1->next;
			tmp1->next = tmp2;
			return (tmp2);
		}
	}
	return NULL;
}
