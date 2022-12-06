#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head node
 * Return: 1 if palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int arrayNum[10240];
	int i = 0, j = 0, m, size = 0;

	if (head == NULL) /* list doesn't exist */
		return (0);
	if (*head == NULL)/* if empty list, then it's a palindrome */
		return (1);

	while (current != NULL)
	{
		current = current->next;
		size++;
	}
	if (size == 1)
		return (1);

	while (current != NULL)
	{
		arrayNum[i] = current->n;
		current = current->next;
		i++;
	}
	if (i % 2 != 0)
		return (0);
	i--;
	m = i / 2;
	for (; j <= m; j++)
	{
		if (arrayNum[j] != arrayNum[i])
			return (0);
		i--;
	}
	return (1);
}
