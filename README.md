# Python_practice
In this repository, I have added solutions to the problems asked in the coding assessment test 

Question 1 -

Jack is a kid and very much likes candies. His uncle gifted him a box of candies of quantity N. There are different types of candies in multiple quantities. Each type is represented by a number in array. Let say, he was gifted 5 candies: 11222. Jack's other has put limitations on the number of candies to be consumed each day. As per her mother, he can eat only 1 type of candies each day, and can eat max 2 candies of each type. Jack wants to finish the candies as soon as possible. Find the minimum number of days in which jack can finish the all the candies.

Example 1:

Input:

5 - Value of N i.e., Number of candies.
11222 - a[] Elements a[O] to a[N-1). where each input element is separated by new line.

Output:  3

Explanation:
There are 2 different kind of candies, two 1's and three 2's. Jack is allowed to consume at max 2 candies of same kind, so he can consume two 1's on same day, and two 2's on another day. Only one 2's will be left, which can be consumed on third day. So, the total number of days required will be 3.

Example 2

Input:

5 - Value of Ni.e., Number of candies.
12345 - a[], Elements a[0]to a[N-1],where each input element is separated by new line.

Output: 5

Explanation:
Here all the candies are of different types. He can only consume 1 candy each day in the above scenario, as there are no 2 candies of same types. So, the total number of days required will be 5.
