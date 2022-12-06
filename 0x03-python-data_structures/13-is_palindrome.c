#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to head node
 * Return: 1 if palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *arrayNum;
	int i = 0, j = 0, k = 0, m;

	while (current != NULL)
	{
		current = current->next;
		k++;
	}
	arrayNum = malloc(sizeof(int) * k);
	if (!arrayNum)
		exit(98);

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
	free(arrayNum);
	return (1);
}

