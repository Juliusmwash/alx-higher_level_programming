listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp1, *tmp2, *tmp3;

	tmp1 = *head;
	tmp2 = malloc(sizeof(listint_t));
	if (tmp2 == NULL)
		return (NULL);
	tmp2->n = number;

	if ((*head)->n > number)
	{
		tmp2->next = *head;
		*head = tmp2;
		return (tmp2);
	}
	else if ((*head)->next == NULL)
	{
		tmp2->next = NULL;
		(*head)->next = tmp2;
		return (tmp2);
	}
	else
		free(tmp2);
	while (tmp1 != NULL)
	{
		tmp2 = malloc(sizeof(listint_t));
		if (tmp2 == NULL)
			return (NULL);
		tmp2->n = number;
		if (tmp1->next->n < number)
		{
			tmp1 = tmp1->next;
			if (tmp1->next  == NULL)
			{
				tmp2->next = NULL;
				tmp1->next = tmp2;
				return (tmp2);
			}
		}
		else
		{
			tmp2->next = tmp1->next;
			tmp1->next = tmp2;
			return (tmp2);
		}
		free(tmp2);

	}
	return NULL;
}
