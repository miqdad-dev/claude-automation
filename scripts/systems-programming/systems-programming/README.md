# Threaded Merge Sort in C

The project is a simple implementation of Merge Sort algorithm using threads in C. Given an array of numbers, it sorts the numbers in ascending order.

## How it Works

The program creates a new thread for each recursive call to the merge sort function. The threaded merge sort function takes a structure as argument which contains the indices of the start and end of the array segment to sort. The array is sorted in-place.

## How to Run

Ensure you have `gcc` installed on your machine. Run the following commands to compile and run the program: