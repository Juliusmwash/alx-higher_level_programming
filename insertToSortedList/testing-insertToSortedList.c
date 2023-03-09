#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */


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

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
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
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
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
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 1025);
    insert_node(&head, 27);
    insert_node(&head, -1);
    insert_node(&head, 99);

    print_listint(head);

    free_listint(head);

    return (0);
}
