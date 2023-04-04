
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = int(input("Enter your number here : "))
def f2(data):
    comm.send(data, dest=1, tag=11)
    if rank == 1:
        data = comm.recv(source=0, tag=11)

    
f2()