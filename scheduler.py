# The Process class represents a single process in the system.
# Each process has a unique process id (pid), an arrival time, a burst time, a priority, and a remaining time.
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

#The fcfs_scheduling function implements the first-come-first-serve scheduling algorithm.
#It sorts the processes by arrival time and then schedules them in that order.
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)

    # Initialize the current time, total turnaround time, and total waiting time
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    # Loop through each process in the list
    for process in processes:
        # If the current time is less than the arrival time of the process, then set the current time to the arrival time of the process
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        
        # Calculate the waiting time and the turnaround time for the process
        waiting_time = current_time - process.arrival_time
        total_waiting_time += waiting_time

        # Update the current time by adding the burst time of the process
        current_time += process.burst_time

        # Calculate the turnaround time for the process and add it to the total turnaround time
        turnaround_time = current_time - process.arrival_time
        total_turnaround_time += turnaround_time

        # Print the details of the process
        print(f"Process {process.pid} finished at {current_time}")
        print(f"Turnaround time: {turnaround_time}")
        print(f"Waiting time: {waiting_time}")
        print("--------------------------------------------------------------")
    
    # Calculate the average turnaround time and the average waiting time
    average_turnaround_time = total_turnaround_time / len(processes)
    average_waiting_time = total_waiting_time / len(processes)

    # Print the average turnaround time, the average waiting time, and the throughput
    print(f"Average turnaround time: {average_turnaround_time}")
    print(f"Average waiting time: {average_waiting_time}")
    print(f"Throughput: {len(processes) / current_time}")

# Round Robin Scheduling
def round_robin_scheduling(processes, quantum):
    # get the number of processes
    n = len(processes)
    # sort the processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)
    # initialize the current time, the queue, the index, the total turnaround time, and the total waiting time
    current_time = 0
    queue = []
    i = 0
    total_turnaround_time = 0
    total_waiting_time = 0

    # Loop until all processes have been scheduled
    while i < n or queue:
        # Add all processes that have arrived to the queue
        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1
        # If there are processes in the queue, then schedule the first process in the queue
        if queue:
            # Get the next process in the queue
            process = queue.pop(0)
            # Calculate the waiting time for the process
            waiting_time = current_time - process.arrival_time
            total_waiting_time += waiting_time

            # If the remaining time of the process is greater than the quantum, then schedule the process for the quantum
            if process.remaining_time > quantum:
                # Advance the current time by the quantum and decrease the remaining time of the process by the quantum
                current_time += quantum
                process.remaining_time -= quantum
                # Add the process back to the queue
                queue.append(process)
            else:
                # Advance the current time by the remaining time of the process
                current_time += process.remaining_time
                # Calculate the turnaround time for the process and add it to the total turnaround time
                turnaround_time = current_time - process.arrival_time
                total_turnaround_time += turnaround_time
                # Print the details of the process
                print(f"Process {process.pid} finished at {current_time}")
                print(f"Turnaround time: {turnaround_time}")
                print(f"Waiting time: {waiting_time}")
                print("--------------------------------------------------------------")
        else:
            # If there are no processes in the queue, then set the current time to the arrival time of the next process
            current_time = processes[i].arrival_time
    # Calculate the average turnaround time and the average waiting time
    average_turnaround_time = total_turnaround_time / n
    average_waiting_time = total_waiting_time / n
    # Print the average turnaround time, the average waiting time, and the throughput
    print(f"Average turnaround time: {average_turnaround_time}")
    print(f"Average waiting time: {average_waiting_time}")
    print(f"Throughput: {len(processes) / current_time}")
    
# Shortest Remaining Time First Scheduling
def srtf_scheduling(processes):
    # get the number of processes
    n = len(processes)
    # sort the processes by arrival time
    processes.sort(key=lambda x: x.arrival_time)
    # initialize the current time, the queue, the index, the total turnaround time, and the total waiting time
    current_time = 0
    queue = []
    i = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    # initialize a dictionary to keep track of the last finish time of each process
    last_process_finish_time = {process.pid: process.arrival_time for process in processes}

    # Loop until all processes have been scheduled
    while i < n or queue:
        # Add all processes that have arrived by the current time to the queue
        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1
        # If there are processes in the queue, then schedule the process with the shortest remaining time
        if queue:
            queue.sort(key=lambda x: x.remaining_time)
            # Get the process with the shortest remaining time from the queue
            process = queue.pop(0)
            # Calculate the waiting time for the process and add it to the total waiting time
            waiting_time = current_time - last_process_finish_time[process.pid]
            total_waiting_time += waiting_time

            # If the remaining time of the process is greater than 1, then schedule the process for 1 unit of time
            if process.remaining_time > 1:
                # Advance the current time by 1 unit of time and decrease the remaining time of the process by 1 unit of time
                current_time += 1
                process.remaining_time -= 1

                # Update the last finish time of the process
                last_process_finish_time[process.pid] = current_time
                # Add the process back to the queue
                queue.append(process)
            else:
                # Advance the current time by the remaining time of the process
                current_time += process.remaining_time
                # Calculate the turnaround time for the process and add it to the total turnaround time
                turnaround_time = current_time - process.arrival_time
                total_turnaround_time += turnaround_time
                # Print the details of the process
                print(f"Process {process.pid} finished at {current_time}")
                print(f"Turnaround time: {turnaround_time}")
                print(f"Waiting time: {waiting_time}")
                print("--------------------------------------------------------------")
        else:
            # If there are no processes in the queue, then set the current time to the arrival time of the next process
            current_time = processes[i].arrival_time
    # Calculate the average turnaround time and the average waiting time
    average_turnaround_time = total_turnaround_time / n
    average_waiting_time = total_waiting_time / n
    # Print the average turnaround time, the average waiting time, and the throughput
    print(f"Average turnaround time: {average_turnaround_time}")
    print(f"Average waiting time: {average_waiting_time}")
    print(f"Throughput: {len(processes) / current_time}")

#The take_input function takes input from the user to enter the details for each process.
#It returns a list of processes.
def take_input():
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append(Process(i + 1, arrival_time, burst_time))
    return processes

#The main function is the entry point of the program.
#It takes input from the user and then calls the scheduling functions.
def main():
    processes = take_input()

    print("\nFCFS Scheduling:")
    fcfs_scheduling(processes[:])

    print("\nRound Robin Scheduling:")
    round_robin_scheduling(processes[:], quantum=2)

    print("\nShortest Remaining Time First Scheduling:")
    srtf_scheduling(processes[:])

#This line checks if this file is the main program file.
#If it is, then it calls the main function to start the program.
if __name__ == "__main__":
    main()