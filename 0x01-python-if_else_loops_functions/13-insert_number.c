#include "lists.h"

/**
 * insert_node - inserts a number in a sorted linked list
 * @head: pointer to head node
 * @number: number to be inserted
 * Return: address of new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new;
	listint_t *temp;

	current = *head;
	temp = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->n >= new->n)
			{
				new->next = current;
				if (temp)
					temp->next = new;
				else
					*head = new;
				return (*head);
			}
			temp = current;
			current = current->next;
		}
		current->next = new;
	}

	return (*head);
}
