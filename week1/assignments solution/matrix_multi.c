#include <stdlib.h>
#include <stdio.h>


#define n 12
#define m 6

double a[n][m];
double b[m][n];
double c[n][n];

int main()
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
		{
			a[i][j] = (double)rand() / 1000;
			b[j][i] = (double)rand() / 1000;
		}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			c[i][j] = 0;
		}
	for (int i = 0; i < n; i++)
		for (int k = 0; k < n; k++)
		{
			double sum = 0;
			for (int j = 0; j < m; j++)
				sum += a[i][j] * b[j][k];
			c[i][k] = sum;
		}

	//	#prin t yhe results
	for (int i = 0; i < n; i++){
			for (int j = 0; j < n; j++)
			{
				printf("%f\t", c[i][j] );
			}
			printf("\n");
			}
	return 0;
}
