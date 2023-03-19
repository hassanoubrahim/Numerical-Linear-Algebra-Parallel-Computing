#include <stdlib.h>


#define n 1024
#define BLOCK_SIZE 32

double a[n][n];
double b[n][n];
double c[n][n];

int main()
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
		{
			a[i][j] = (double)rand() / 1000;
			b[i][j] = (double)rand() / 1000;
			c[i][j] = 0;
		}
	for (int i0 = 0; i0 < n; i0 += BLOCK_SIZE)
	    for (int j0 = 0; j0 < n; j0 += BLOCK_SIZE)
		for (int k0 = 0; k0 < n; k0 += BLOCK_SIZE)
		    for (int i = i0; i < i0 + BLOCK_SIZE && i < n; i++)
		        for (int j = j0; j < j0 + BLOCK_SIZE && j < n; j++)
		        {
		            double sum = 0;
		            for (int k = k0; k < k0 + BLOCK_SIZE && k < n; k++)
		                sum += a[i][k] * b[k][j];
		            c[i][j] += sum;
		        }
	return 0;
}
