from mpi4py import MPI

# Initialize the MPI environment
comm = MPI.COMM_WORLD

# Get the rank of the process (process ID)
rank = comm.Get_rank()

# Get the total number of processes
size = comm.Get_size()

# Master Process
if rank == 0:
    # Sending messages to all processes except the master itself
    for i in range(1, size):
        message = f"Hello from Master to Process {i}"
        comm.send(message, dest=i)
        print(f"Master sent: {message}")

    # Receiving messages from all slave processes
    for i in range(1, size):
        received_message = comm.recv(source=i)
        print(f"Master received: {received_message}")

# Slave Processes
else:
    # Receiving a message from the master process
    received_message = comm.recv(source=0)
    print(f"Process {rank} received: {received_message}")

    # Sending a message back to the master
    response_message = f"Hello Master, this is Process {rank}"
    comm.send(response_message, dest=0)


# OUTPUT

"""
Master sent: Hello from Master to Process 1
Master sent: Hello from Master to Process 2
Master sent: Hello from Master to Process 3

Master received: Hello Master, this is Process 1
Master received: Hello Master, this is Process 2
Master received: Hello Master, this is Process 3

Process 1 received: Hello from Master to Process 1
Process 2 received: Hello from Master to Process 2
Process 3 received: Hello from Master to Process 3
"""