
from mpi4py import MPI
import numpy as np


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def f4(n = 6, m = 4, sendcounts = None, displs = None, recvcount = None, recvbuf = None):

    if rank == 0:
        # create matrix A
        A = np.arange(n * m).reshape(n, m)

        # calculate sendcounts and displs
        sendcounts = np.full(size, n * m // size, dtype=int)
        sendcounts[-1] = n * m - sendcounts[:-1].sum()
        displs = np.concatenate(([0], np.cumsum(sendcounts[:-1])))

        # scatter A using MPI_Scatterv
        comm.Scatterv([A, sendcounts, displs, MPI.INT], None, root=0)

    else:
        # determine the receive buffer size and create the receive buffer
        if rank == 1 or rank == 2:
            recvcount = n * (m // 2)
        else:
            recvcount = (n // 2) * (m // 2)
        recvbuf = np.empty(recvcount, dtype=int)

        # receive the data using MPI_Scatterv
        comm.Scatterv(None, [recvbuf, sendcounts, displs, MPI.INT], root=0)

        # print the received data
        if rank == 1:
	        print(f"Rank {rank} received:")
	        for i in range(n // 2):
	        	for j in range(m // 2, m):
	        		print(f"{recvbuf[i * (m // 2) + j - m // 2]} ", end="")
	        	print("")
        elif rank == 2:
            print(f"Rank {rank} received:")
            for i in range(n // 2, n):
            	for j in range(m // 2):
            		print(f"{recvbuf[(i - n // 2) * (m // 2) + j]} ", end="")
            	print("")
        elif rank == 3:
            print(f"Rank {rank} received:")
            for i in range(n // 2, n):
                for j in range(m // 2, m):
                    print(f"{recvbuf[(i - n // 2) * (m // 2) + j - m // 2]} ", end="")
                print("")



f4()
