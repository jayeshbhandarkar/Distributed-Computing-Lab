from mpi4py import MPI

def main():
    # Initialize the MPI environment
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()  # Get the rank of the process
    size = comm.Get_size()  # Get the total number of processes

    if size < 2:
        print("This program requires at least 2 processes.")
        return

    if rank == 0:
        # Process with rank 0 sends a message
        message = "Hello from process 0"
        comm.send(message, dest=1, tag=0)
        print(f"Process {rank} sent: {message}")

    elif rank == 1:
        # Process with rank 1 receives the message
        message = comm.recv(source=0, tag=0)
        print(f"Process {rank} received: {message}")

if __name__ == "__main__":
    main()


# OUTPUT

"""
Process 0 sent: Hello from process 0
Process 1 received: Hello from process 0
"""