# Python_practice
In this repository, I have added solutions to the problems asked in the coding assessment tests.

## Question 1 -

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


## Question 2 - 

Given the alphanumeric string str, the task is to check how many even numbers are there in the string. Write a program to count the even numbers from alphanumeric string and print it.

Example 1 :
Input: ABCD4573HDc82Hr6 ► Alphanumeric String

Output :  
4

Explanation: ABCD4573HDc82Hr6 is an alphanumeric number. There is total 4 even number (4,8,2,6). Hence, the output is 4.

Example 2 :

Input:
Bca77b3c5a ► Alphanumeric String

Output :  
0

## Question 3 -

Touka is fan of big numbers, so when her friend kuroko gives her a positive number N she calculates M = 2^N (2 raised to power N) and tell it to him .But since M can be very large so it is very difficult for her to tell it to kuroko. So she decides to calculate the sum of digits of M till she gets a single digit number and tells it to kuroko.
Touka is very tired of the calculation and needs your help to calculate it for her. Her friend kuroko asks her T queries. In each query you will be given N as input. Print the answer reqired in each query.

Example : 
Let's assume that N=6 then M = 2^6 = 64. Now 6+4=10. Since it's still not a single digit so we add digits of 10 ie 1+0=1, which is the required answer.

Function Description : 
Complete the solve function provided in the editor. This function takes the following 1 parameter and returns the sum of digits of M untill its a single digit number.

## Question 4 - 

Charging Phone

You have to find the amount of time it takes to charge a smartphone to charge level atleast T. given its initial charge level S. But the charger is smart, and charges at different rates depending on the charge level in smartphone to prevent damage to the battery. You are given a smartphone with an efficient charger. The initial amount of charge in the smartphone is S. It charges the smartphone at different rates depending upon the amount of charge available in the phone to prevent the battery of the phone from any damage. Assuming that the current amount of charge available in the phone is C. the rates at which the phone is charged R in units per minute are as follows. Assuming current charge level is the rates R of charging are (in units per minute)

0 <= C <= 10. R = 10
11 <= C <= 230, R = 5
231 <= C <= 559, R = 8
560 <= C <= 1009, R = 2
1010 <= C <= 5000, R = 7
5001 <= C <= 10000, R = 8
10001 <= C <= 10**9, R = 3
