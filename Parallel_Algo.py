import multiprocessing

# Function to calculate the sum of squares of a given list of numbers
def sum_of_squares(numbers, result, index):
    total = sum(x * x for x in numbers)
    result[index] = total

# Function to compute the sum of squares in parallel
def parallel_sum_of_squares(numbers, num_processes):
    # Split the data into chunks for each process
    chunk_size = len(numbers) // num_processes
    chunks = [numbers[i * chunk_size : (i + 1) * chunk_size] for i in range(num_processes)]

    # If there are remaining elements, add them to the last chunk
    if len(numbers) % num_processes != 0:
        chunks[-1].extend(numbers[num_processes * chunk_size:])

    # Create a result array to hold the results from each process
    result = multiprocessing.Array('i', num_processes)

    processes = []
    for i in range(num_processes):
        # Create a process for each chunk
        p = multiprocessing.Process(target=sum_of_squares, args=(chunks[i], result, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    # Combine results
    total_sum = sum(result)
    return total_sum

if __name__ == "__main__":
    n = int(input("How many numbers?: "))
    numbers = list(range(1, n + 1))  # Example list of numbers
    num_processes = multiprocessing.cpu_count()  # Use as many processes as CPU cores

    total = parallel_sum_of_squares(numbers, num_processes)
    print(f"The sum of squares is: {total}")
