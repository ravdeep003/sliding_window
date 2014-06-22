sliding_window
==============
Problem Statement:
We have a stream of numbers coming in and we have a sliding window of size N, which slides to the right. We need to output the smallest number in every window.

For example consider the following stream of numbers and a window size of 3

10 4 18 2 6 19 24 1 20

The output must be

4 2 2 2 6 1 1

Your input will from a file in which the first line will contain the window size N, the second line will contain a stream of numbers separated by space. You need to output the smallest numbers in each window separated by space.

Sample Input:
3
10 4 18 2 6 19 24 1 20

Expected Output:
4 2 2 2 6 1 1