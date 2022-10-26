# Lab 2 and 3: Implementing a decision problem

Problem: We have two containers of capacity m liters and n liters respectively and an unlimited amount of water. Determine a sequence of filling the containers and pouring from one container into the other (until it is full) or on the ground, so that k liters remain in one of the containers. We have no other method of measuring a quantity of water.

Requirements:

1. Choose a representation of a state of the problem. The representation must be explicit enough to contain all the necessary information to continue finding a solution, but it must also be formalized enough to be easy to process/store.
2. Identify the special states (initial and final) and implement the initialization function (gets as parameters the instance m, n and k, returns the initial state) and the boolean function that checks whether a state received as a parameter is final.
3. Implement transitions as functions that get as parameters a state (and additional ones, if needed) and return the state resulting from applying the transition. Validation of transitions is done in one or more boolean functions with the same parameters.
4. Implement the Backtracking strategy.
5. Implement the BFS strategy.
6. Implement the Hillclimbing strategy.
7. Implement strategy A\*
8. Implement a menu that allows, after entering the instance, to select the strategy to be tried.
9. (Bonus) Implement a boolean function that checks for an instance received as parameter whether or not we can find a solution.

When displaying the solution, all the transitions made will be indicated, one by one.
For the first lab at least the first two points must be solved.
For the second lab, at least the first 5 points must be solved.

Useful resources:
https://www.interviewbit.com/blog/water-jug-problem/
