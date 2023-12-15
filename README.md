<h1 align="center"> Process Scheduler Simulator </h1>

<p align="center">
  <em>Comparing the efficiency of algorithms<br>CS-630-003: Team A19</em>
</p>

## Overview
This project aims to simulate a process scheduler utilizing various scheduling algorithms such as First Come First Serve (FCFS), Round Robin, and Shortest Remaining Time First (SRTF). The purpose is to visualize the scheduling of processes and compare the efficiency of these algorithms in managing the order and execution of processes within a computing environment.

The project will be written in Python.

## Features
This project will explore three different scheduling algorithms:
1. <b>FCFS (First Come First Serve)</b>: Processes are executed in the order they arrive in the ready queue.
2. <b>Round Robin</b>: The scheduler has an assigned time slice for each process and evenly allocates and cyles through each process until all are completed.
3. <b>SRTF (Shortest Remaining Time First)</b>: Processes are executed in the order of their remaining time, shortest remaining time being executed first.
## Requirements
This project requires Python 3.6 or later. No additional libraries are required.
This project was created in Visual Studio Code.
## Usage
To use this project:
1. First clone the repository using `git clone https://github.com/Dortiz246/Process_Scheduler_Simulator.git` in the terminal of your IDE <b>(VSCode in this case)</b>.
2. Then, you can run the scheduling algorithms with your own inputs when you run the scheduler.py file.
3. To run the scheduler.py file you can use ctrl+f5 or press the run button on the top right corner if using VSCode.
4. Enter how many processes you want to simulate.
5. Following the prompts enter the respective arrival time and burst time (execution time) for each process.
6. Program will run each algorithm with the inputted information and print the results.
## File Structure
1. README.md: Readme file containing information such as requirements, features, and steps to run the program.
2. scheduler.py: Contains all of the functios to simulate the logic each process, take user input, and run each process with the inputted information.
3. Program follows monolithic approach due to time constraints.
## Contributions
Members of Team A19 include:
1. Darryl Ortiz
2. Hari Chandana Reddy Sanikommu
3. Rohan Chopra
4. Siddhant Kumar Soam 
