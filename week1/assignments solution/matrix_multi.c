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
		for (int j = 0; j < n; j++)
			for (int k = 0; k < n; k++)
				c[i][j] += a[i][k]*b[k][j];
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
