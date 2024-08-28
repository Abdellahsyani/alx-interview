# 0x05. N Queens
* The “0x05. N queens” project is a classic problem in computer science and mathematics, known for its application of the backtracking algorithm to place N non-attacking queens on an N×N chessboard. To successfully complete this project, you will need to understand several key concepts and have access to resources that will help you grasp the necessary algorithms and techniques.

## Conceepts Needed:
* [Backtracking Introduction](https://www.geeksforgeeks.org/introduction-to-backtracking-2/)
* [Recursion in Python](https://realpython.com/python-thinking-recursively/)
* [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)
* [Command Line Arguments in Python](https://docs.python.org/3.3/library/sys.html#sys.argv)

* By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

## Additional Resources
* [Mock Interview](https://www.youtube.com/watch?feature=shared&v=GneS80iYa7I)

## The task

* [0-nqueens.py](0-nqueens.pu)

* The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

* Usage: `nqueens N`
* If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status `1`
* where N must be an integer greater or equal to `4`
- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
- If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`
* The program should print every possible solution to the problem
 	One solution per line
 	Format: see example
	You don’t have to print the solutions in a specific order
* You are only allowed to import the `sys` module
* Read: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)

`julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
 [[0, 1], [1, 3], [2, 0], [3, 2]]
 [[0, 2], [1, 0], [2, 3], [3, 1]]
 julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
 [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
 [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
 [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
 [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
 julien@ubuntu:~/0x08. N Queens$`
