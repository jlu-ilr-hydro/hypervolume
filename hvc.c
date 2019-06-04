#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdarg.h>
#include <time.h>
#include <math.h>
#include <pthread.h>
#include <stdbool.h>
#include "hv.h"

double *data_maximum(double *data, int nobj, int rows)
{
    double *vector;
    int n, r, k;

    vector = malloc(nobj * sizeof(double));

    for (k = 0; k < nobj; k++)
        vector[k] = data[k];

    for (r = 1; r < rows; r++)
    {
        for (n = 0; n < nobj; n++, k++)
        {
            if (vector[n] < data[k])
                vector[n] = data[k];
        }
    }
    return vector;
}

double hvc(double **py_list, int dim_x, int dim_y)
{

    //int n = 2; // dim_x
    //int d = 4; // dim_y

    double *dyn_array = malloc(dim_x * dim_y * sizeof(double));

    // we need a reshape for this funny tool
    int k = 0;
    for (int i = 0; i < dim_y; i++)
        for (int j = 0; j < dim_x; j++)
            dyn_array[k++] = py_list[i][j];

    /*for (int j = 0; j < dim_x * dim_y; j++)
    {
        printf("debug: %f\n", dyn_array[j]);
    }*/

    // make a reference array
    double *res = data_maximum(dyn_array, dim_x, dim_y);

    double vol = fpli_hv(dyn_array, dim_x, dim_y, res);

    // clean up memory
    free(res);
    free(dyn_array);

    return vol;
}