
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = None

if rank == 0:
    data = int(input("enter value"))
    comm.send(data, dest=(rank+1))
    print(f"process {rank} send data {data}")
else:
    data = comm.recv(source=(rank-1))
    print(f"process {rank} recv data {data}")
    data = data+rank
    if rank == size-1:
        print(f"final data : rank = {rank} and data = {data}")
    else:
        comm.send(data, dest=(rank+1))
        print(f"process {rank} send data {data}")


