# 0x08-making change 

* For the “0. Change comes from within” project, you will tackle a classic problem from the domain of dynamic programming and greedy algorithms: the coin change problem. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. This project challenges you to apply your understanding of algorithms to devise a solution that is not only correct but also efficient. Below are the key concepts and resources necessary to complete this project successfully.

## Concepts Needed:
### 1.Greedy Algorithms:

* Understanding how greedy algorithms work and why they are suitable for the coin change problem.
* Recognizing the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.
### 2.Dynamic Programming:

* Basic principles of dynamic programming as a method to solve optimization problems.
* The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.
### Algorithmic Complexity:

* Analyzing the time and space complexity of algorithms.
* Striving for solutions with lower complexity to meet runtime constraints.
### Problem-Solving Strategies:

* Breaking down the problem into smaller, manageable sub-problems.
* Iterative vs recursive approaches to dynamic programming.
### Python Programming:

* Manipulating lists and using list comprehensions.
* Implementing functions with efficient looping and conditional statements.

## Resources

* Python Official Documentation:

* [More Control Flow Tools (for loops, if statements)](https://docs.python.org/3/tutorial/controlflow.html)
* GeeksforGeeks Articles:

* [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
* [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
* YouTube Tutorials:

* [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jgiZlGzXMBw) for a visual and step-by-step explanation of the dynamic programming approach.

* By thoroughly understanding these concepts and utilizing the provided resources, you will be well-prepared to tackle the coin change problem. You will need to decide whether a greedy algorithm suffices for your particular set of coin denominations or if a more comprehensive dynamic programming approach is necessary to ensure correctness and efficiency. This project not only tests algorithmic skills but also reinforces the importance of choosing the right strategy based on problem constraints.

## Additional Resources
* [Mock Technical Interview](https://www.youtube.com/watch?feature=shared&v=9BSSIsJ-fWg)

## Requirements
* General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `PEP 8` style (version 1.7.x)
* All your files must be executable

## Tasks

+ [x] 0. **Change comes from within**<br/>[0-making change.py](0-making_change.py) contains a module with a function that determines the fewest number of coins needed to meet a given amount `total` when given a pile of coins of different values, with the following requirements:
  + Prototype: def makeChange(coins, total)
  + Return: fewest number of coins needed to meet total
    + If total is 0 or less, return 0
    + If total cannot be met by any number of coins you have, return -1
  + coins is a list of the values of the coins in your possession
  + The value of a coin will always be an integer greater than 0
  + You can assume you have an infinite number of each denomination of coin in the list
  + Your solution’s runtime will be evaluated in this task
```
carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$
```
