#include "mpi.h"
#include <stdio.h>
#define MASTER 0
#define N 5

int main(int argc, char* argv) {
	int numprocs, procid, rc, i, aux;
	int sum_total = 0;
	MPI_Status status;
	int v[20] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
	//char hostname[MPI_MAX_PROCESSOR_NAME];

	rc = MPI_Init(&argc,&argv);
	if(rc != MPI_SUCCES) {
		printf("Error starting. \n");
		MPI_Abort(MPI_COMM_WORLD, rc);
	}

	MPI_Comm_size(MPI_COMM_WORLD, &numprocs);
	MPI_Comm_rank(MPI_COMM_WORLD, &procid);

	//m
	if(procid == MASTER) {
		for(int p = 1; p < numprocs; p++) {
			MPI_Send(&v[p*(N/numprocs)], N / numprocs, MPI_INT, p, 1, MPI_COMM_WORLD);  
		}
		for (int i = 0; i < N / numprocs; i++)
			sum_total += v[i];
		for(int p = 1; p < numprocs; p++) {
			MPI_Recv(&aux, 1, MPI_INT, p, 1, MPI_COMM_WORLD, &status);  
			sum_total = sum_total + aux;
		}

		printf("sum = %d", sum_total);
	}

	//s
	else{
		int sum = 0;
		MPI_Recv(v, N / numprocs, MPI_INT, 0, 1, MPI_COMM_WORLD, &status);  
		for (i = 0; i < N / numprocs; i++) {
			sum = sum + v[i];
		}
		MPI_Send(&sum, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);  
	}
	MPI_Finalize();
}