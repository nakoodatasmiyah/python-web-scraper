# Factorial Calculator

This repository contains a simple Python script (`factorial.py`) that calculates the factorial of a positive integer.

## Problem

The problem this script solves is calculating the factorial of a given positive integer. The factorial of a number `n` (denoted as `n!`) is the product of all positive integers less than or equal to `n`. For example, the factorial of 5 (5!) is `5*4*3*2*1 = 120`.

Factorial calculation is a common mathematical operation and is frequently used in various fields like combinatorics, algebra, and calculus.

## Approach

The script uses a recursive function to solve this problem. The base case of the recursion is `0! = 1`. For all other positive integers `n`, the factorial is calculated as `n * (n-1)!`. This leads to a series of recursive calls until the base case is reached.

## How to Run

You can run the script using any Python3 interpreter. The script currently calculates the factorial of 5, but you can change the input to calculate the factorial of any other positive integer.

