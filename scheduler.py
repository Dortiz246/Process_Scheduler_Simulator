# The Process class represents a single process in the system.
# Each process has a unique process id (pid), an arrival time, a burst time, a priority, and a remaining time.
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time

#The fcfs_scheduling function implements the first-come-first-serve scheduling algorithm.
#It sorts the processes by arrival time and then schedules them in that order.
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        current_time += process.burst_time
        print(f"Process {process.pid} finished at {current_time}")

#The sjf_scheduling function implements the shortest-job-first scheduling algorithm.
#It sorts the processes by arrival time and then burst time and then schedules them in that order.
def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        current_time += process.burst_time
        print(f"Process {process.pid} finished at {current_time}")

#The priority_scheduling function implements the priority scheduling algorithm.
#It sorts the processes by arrival time and then priority and then schedules them in that order.
def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        current_time += process.burst_time
        print(f"Process {process.pid} finished at {current_time}")

#The take_input function takes input from the user to enter the details for each process.
#It returns a list of processes.
def take_input():
    num_processes = int(input("Enter the number of processes: "))
    processes = []
    for i in range(num_processes):
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        priority = int(input(f"Enter priority for process {i + 1}: "))
        processes.append(Process(i + 1, arrival_time, burst_time, priority))
    return processes

#The main function is the entry point of the program.
#It takes input from the user and then calls the scheduling functions.
def main():
    processes = take_input()

    print("\nFCFS Scheduling:")
    fcfs_scheduling(processes[:])

    print("\nSJF Scheduling:")
    sjf_scheduling(processes[:])

    print("\nPriority Scheduling:")
    priority_scheduling(processes[:])

#This line checks if this file is the main program file.
#If it is, then it calls the main function to start the program.
if __name__ == "__main__":
    main()